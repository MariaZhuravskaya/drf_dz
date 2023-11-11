import os

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from payments.models import Payments
from payments.serializers import PaymentsSerializers
import stripe


class PaymentsListView(generics.ListAPIView):
    """
    Представление для просмотра списка платежей
    """
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializers
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['payment_method', 'payment_course_lesson']
    ordering_fields = ['date']


class PaymentsRetrieveView(generics.RetrieveAPIView):
    """
    Представление для просмотра платежа
    """
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializers


class PaymentsCreateView(generics.CreateAPIView):
    """
    Представление для создания платежа
    """
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializers

    def perform_create(self, serializer):
        """
        Метод для создания объекта PaymentIntent
        """
        payment = serializer.save()
        stripe.api_key = os.getenv('API_KEY')
        pay = stripe.PaymentIntent.create(
            amount=payment.payment_amount,
            currency="usd",
            payment_course=payment.payment_course,
            #automatic_payment_methods={"enabled": True},
            confirm=True,
            payment_method="pm_card_visa",
            return_url="http://localhost:8000/payments/return_url",
        )
        pay.save()
        return super().perform_create(serializer)


class PaymentsDestroyView(generics.DestroyAPIView):
    """
    Представление для удаления платежа
    """
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializers


class GetPaymentView(APIView):
    """
    Получение информации о платеже.

    get:
    Получает информацию о платеже по его ID.
    """

    def get(self, request, payment_id):
        payment_intent = stripe.PaymentIntent.retrieve(payment_id)
        return Response({
            'status': payment_intent.status,
            'body': payment_intent})