from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('test-payment/', views.test_payment)
]
