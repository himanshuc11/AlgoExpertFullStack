from django.contrib import admin
from .models import ProblemList, AlgoExpertUser, ProblemTags, AlgoExpertUserSolution

# Register your models here.
admin.site.register(ProblemList)
admin.site.register(AlgoExpertUser)
admin.site.register(ProblemTags)
admin.site.register(AlgoExpertUserSolution)