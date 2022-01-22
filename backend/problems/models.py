from pyexpat import model
from django.db import models

# Create your models here.
class ProblemTags(models.Model):
    tag = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.tag}"

difficulty = [
    ('EASY', 'EASY'),
    ('MEDIUM', 'MEDIUM'),
    ('HARD', 'HARD'),
    ('VERY HARD', 'VERY HARD')
]
TIER_CHOICES = [
    ('F', 'FREE'),
    ('P', 'PAID')
]

class ProblemList(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    sample_cases = models.CharField(max_length=2048)
    test_cases = models.TextField()
    solution = models.TextField()
    start_code = models.TextField()
    tier = models.CharField(max_length=16,choices=TIER_CHOICES, default='P')
    difficulty = models.CharField(max_length=64, choices=difficulty)
    tags = models.ManyToManyField(ProblemTags)


    def __str__(self):
        return f"{self.name}"

class AlgoExpertUser(models.Model):
    email = models.EmailField(max_length=2048, unique=True)
    tier = models.CharField(max_length=16,choices=TIER_CHOICES, default='F')

    def __str__(self):
        return f"{self.email}: {self.tier}"

class AlgoExpertUserSolution(models.Model):
    user = models.ForeignKey(AlgoExpertUser, on_delete=models.CASCADE)
    problem = models.ForeignKey(ProblemList, on_delete=models.CASCADE, related_name="user_submission")
    solution = models.TextField()

    def __str__(self):
        return f"{self.user} {self.problem}"



