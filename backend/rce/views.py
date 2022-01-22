from django.http import HttpResponse
from problems.models import ProblemList
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Q
import subprocess
import os

from problems.models import AlgoExpertUser, AlgoExpertUserSolution, ProblemList

# Create your views here.
# def python(request):
#     problem = ProblemList.objects.get(id=1)

#     code = ""
#     with open('rce/code.py', 'r') as file:
#         code = file.read()

#     with open('rce/rce_test.py', 'w') as file:
#         file.write(code)
#         file.write('\n\n')
#         file.write(problem.test_cases)
        
#     out = subprocess.Popen(['python3', 'rce/rce_test.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     try:
#         stdout, stderr = out.communicate(timeout=3)
#         stdout = stdout.decode('utf-8')
#         stderr = stderr.decode('utf-8')
#         print(stderr)
#     except TimeoutError:
#         out.kill()
#         stdout = stdout.decode('utf-8')
#         stderr = stderr.decode('utf-8')

#     return HttpResponse('Python Code executed here')

class CodeExecutionAPIView(APIView):
    def post(self, request):
        if 'email' not in request.data:
            return Response("Email ID is absent",status.HTTP_400_BAD_REQUEST)
        if 'code' not in request.data:
            return Response("Code is absent",status.HTTP_400_BAD_REQUEST)
        if 'id' not in request.data:
            return Response("Problem id absent", status.HTTP_400_BAD_REQUEST)

        try: 
            user = AlgoExpertUser.objects.get(email=request.data['email'])
        except AlgoExpertUser.DoesNotExist:
            return Response('Valid email required', status.HTTP_400_BAD_REQUEST)
        
        try:
            problem = ProblemList.objects.get(id=request.data['id'])
        except ProblemList.DoesNotExist:
            return Response('Invalid Problem id', status.HTTP_400_BAD_REQUEST)

        if user.tier == "F" and problem.tier == "P":
            return Response('Cannot access this code in free version', status.HTTP_402_PAYMENT_REQUIRED)
        
        # Execute Code in File and return Result
        location = f"rce/{user.email}-{problem.id}.py"
        with open(location, "w") as file:
            file.write(request.data['code'])
            file.write('\n\n')
            file.write(problem.test_cases)
        
        out = subprocess.Popen(['python3', location], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            stdout, stderr = out.communicate(timeout=3)
            stdout = stdout.decode('utf-8')
            stderr = stderr.decode('utf-8')
        except TimeoutError:
            out.kill()
            stdout = stdout.decode('utf-8')
            stderr = stderr.decode('utf-8')

        # Save Code in User Solution
        solution = AlgoExpertUserSolution.objects.filter(Q(user=user)&Q(problem=problem))
        if len(solution) == 0:
              solution = AlgoExpertUserSolution.objects.create(user=user, problem=problem, solution="")
        else:
            solution = solution[0]
        solution.solution = request.data['code']
        solution.save()

        # Delete The file
        os.remove(location)

        return Response(stderr, status=status.HTTP_200_OK)