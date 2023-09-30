import os

import stripe
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, serializers
from rest_framework.filters import OrderingFilter
from rest_framework.views import APIView

from payment.models import Payment
from payment.serializer import PaymentSerializer
from payment.services import PaymentService, PaymentError


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
        # получаем поля из сериализатора
        lesson = serializer.validated_data.get('paid_lesson')
        course = serializer.validated_data.get('paid_course')

        # проверяем, передано ли в тело запроса курс или урок для оплаты
        if not lesson and not course:
            raise serializers.ValidationError({
                'message_error': 'Необходимо заполнить одно из полей "lesson" или "course"'
            })

        serializer.save()
        stripe_handler = PaymentService()

        stripe_response = stripe_handler.create_payment(
            user=self.request.user,
            amount=serializer.validated_data.get('payment_amount'),
        )
        stripe_id = stripe_response.client_secret

        payment_instance = serializer.instance
        payment_instance.stripe_id = stripe_id
        payment_instance.save()


class PaymentRetrieveAPIView(APIView):
    def get(self, request, pk):
        try:
            payment = get_object_or_404(Payment, pk=pk)
            stripe_id = payment.stripe_id

            stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
            payment_intent = stripe.PaymentIntent.retrieve(stripe_id)

            return Response(payment_intent, status=status.HTTP_200_OK)
        except Payment.DoesNotExist:
            return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)

