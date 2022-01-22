from django.urls import path
from .views import *

urlpatterns = [
    path('python/', CodeExecutionAPIView.as_view()),
]
