import os

import stripe
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.filters import OrderingFilter
from rest_framework.views import APIView

from payment.models import Payment, PaymentMethod
from payment.serializer import PaymentSerializer
from payment.services import PaymentService


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['payment_method', 'paid_course', 'paid_lesson']
    ordering_fields = ['payment_date']


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        payment_method = serializer.validated_data.get('payment_method')
        user = self.request.user
        amount = serializer.validated_data.get('payment_amount')

        stripe_handler = PaymentService()
        payment = stripe_handler.create_and_save_payment(
            user=user,
            amount=amount,
            payment_method=payment_method
        )

        if payment_method == PaymentMethod.BANK_TRANSFER:
            # Возвращаем клиенту client_secret для оплаты кредитной картой
            return Response({"client_secret": payment.stripe_id})
        elif payment_method == PaymentMethod.CASH:
            # Возвращаем клиенту подтверждение оплаты наличными
            return Response({"message": "Оплата наличными зарегистрирована успешно."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentRetrieveAPIView(APIView):
    def get(self, request, pk):
        try:
            payment = get_object_or_404(Payment, pk=pk)
            stripe_id = payment.stripe_id

            if stripe_id is not None:
                stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
                payment_intent = stripe.PaymentIntent.retrieve(stripe_id)

                return Response(payment_intent, status=status.HTTP_200_OK)
            else:
                return Response({"error": "PaymentIntent не существует для этого платежа."},
                                status=status.HTTP_400_BAD_REQUEST)
        except Payment.DoesNotExist:
            return Response({"error": "Платеж не найден"}, status=status.HTTP_404_NOT_FOUND)
