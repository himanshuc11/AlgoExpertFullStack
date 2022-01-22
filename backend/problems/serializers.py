from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from .models import AlgoExpertUser, ProblemList, ProblemTags, AlgoExpertUserSolution

class AlgoExpertUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlgoExpertUser
        fields = ['email', 'tier']


class ProblemTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemTags
        exclude = ['id']

class ProblemSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='tag')
    class Meta:
        model = ProblemList
        fields = ['id', 'name', 'difficulty', 'tags', 'tier']

class ProblemDetailSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='tag')
    class Meta: 
        model = ProblemList
        exclude = ['test_cases']

class AlgoExpertUserSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlgoExpertUserSolution
        fields = "__all__"