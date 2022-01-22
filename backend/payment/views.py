from django.shortcuts import render
import stripe
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

stripe.api_key = 'sk_test_51KJEN6SB6ePdcq7girFUfBAJuV727SXDQohVqllYaWvvXFZNySHUGXQKy38LY9MuXAkY58bVt84JzENrydbOVZES00hUXB0AZT'
# Create your views here.

@api_view(['POST'])
def test_payment(request):
    test_payment_intent = stripe.PaymentIntent.create(
    amount=100000, currency='inr', 
    description = "Purchasing Algorithms Expert",
    payment_method_types=['card'],
    receipt_email='test@example.com')
    return Response(status=status.HTTP_200_OK, data=test_payment_intent)