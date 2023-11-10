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

    # def get_payment(self, request, payment_id):
    #     """
    #     Метод получения информации о платеже
    #     """
    #     stripe.api_key = "sk_test_51OARKLKwGyIdGx42RzISiKP4tOWagFLbZsfNMUoVeY0ktA5B3K0xw6W1B7oHM22xlUBD3u1sfnO2VDL5FvynTded00CWr6ZCgv"
    #
    #     payments_retrieve = stripe.PaymentIntent.retrieve(
    #         payment_id,
    #     )
    #     print(payments_retrieve.status)
    #     return Response({
    #         'status': payments_retrieve.status,
    #         'body': payments_retrieve})


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
        stripe.api_key = "sk_test_51OARKLKwGyIdGx42RzISiKP4tOWagFLbZsfNMUoVeY0ktA5B3K0xw6W1B7oHM22xlUBD3u1sfnO2VDL5FvynTded00CWr6ZCgv"
        pay = stripe.PaymentIntent.create(
            amount=payment.payment_amount,
            currency="usd",
            payment_course=payment.payment_course,
            automatic_payment_methods={"enabled": True},
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