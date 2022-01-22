from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Q

from .models import AlgoExpertUser, AlgoExpertUserSolution, ProblemList, ProblemTags
from .serializers import AlgoExpertUserSerializer, ProblemSerializer, ProblemTagSerializer, ProblemDetailSerializer, AlgoExpertUserSolutionSerializer
from problems import serializers

# Create your views here.
class Auth(APIView):
    def get(self, request):
        return Response('Please send a POST request', status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        if "email" in request.data:
            user, _ = AlgoExpertUser.objects.get_or_create(email=request.data['email'])
            serializer = AlgoExpertUserSerializer(user)
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response('uid not present in the request', status.HTTP_400_BAD_REQUEST)

class SetUserTierAPIView(APIView):
    def post(self, request):
        if 'email' not in request.data:
            return Response('Send Email', status.HTTP_400_BAD_REQUEST)
        email = request.data['email']
        user = AlgoExpertUser.objects.get(email=email)
        user.tier = "P"
        user.save()
        serializer = AlgoExpertUserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

class Problems(APIView):
    def get(self, request):
        problems = ProblemList.objects.all()
        serializer = ProblemSerializer(problems, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

class ProblemTagsAPIView(APIView):
    def get(self, request):
        problem_tags = ProblemTags.objects.all()
        serializer = ProblemTagSerializer(problem_tags, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

class EditorAPIView(APIView):
    def get(self, request, id):
        problem = ProblemList.objects.get(id=id)
        serializer = ProblemDetailSerializer(problem)
        return Response(serializer.data, status.HTTP_200_OK)


class OldCodeAPIView(APIView):
    def post(self, request):
        if 'email' not in request.data:
            return Response("Email required",status.HTTP_400_BAD_REQUEST)
        if 'id' not in request.data:
            return Response("ID required", status.HTTP_400_BAD_REQUEST)

        email = request.data['email']
        id = request.data['id']

        user = AlgoExpertUser.objects.get(email=email)
        problem = ProblemList.objects.get(id=id)

        solution = AlgoExpertUserSolution.objects.filter(Q(user=user) & Q(problem=problem))
        if len(solution) == 1:
             serializer = AlgoExpertUserSolutionSerializer(solution[0])
             return Response(serializer.data)
            
        return Response({"not_present": True})