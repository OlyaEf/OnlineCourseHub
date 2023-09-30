import os

import stripe
from rest_framework import status
from rest_framework.response import Response

from payment.models import PaymentMethod, Payment


class PaymentService:
    def __init__(self):
        self.stripe_api_key = os.getenv('STRIPE_SECRET_KEY')

    def create_payment(self, user, amount):
        try:
            stripe.api_key = self.stripe_api_key
            payment_intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='usd',
                automatic_payment_method={"enabled": True},
                description=f'Payment for user: {user}'
            )
            return payment_intent
        except Exception as e:
            raise PaymentError(str(e))

    def save_payment(self, user, amount, payment_method, stripe_id):
        payment = Payment.objects.create(
            user=user,
            payment_amount=amount,
            payment_method=payment_method,
            stripe_id=stripe_id,
        )
        return payment

    @staticmethod
    def retrieve(stripe_id):
        return stripe.PaymentIntent.retrieve(stripe_id)


class PaymentError(Exception):
    pass
