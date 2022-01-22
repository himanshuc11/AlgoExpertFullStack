from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Auth.as_view()),
    path('set-tier/', views.SetUserTierAPIView.as_view()),
    path('all/', views.Problems.as_view()),
    path('tags/', views.ProblemTagsAPIView.as_view()),
    path('<int:id>/', views.EditorAPIView.as_view()),
    path('old/', views.OldCodeAPIView.as_view())
]
