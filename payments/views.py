import os

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter

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
        product = stripe.Product.create(name=payment.payment_course.name)
        price = stripe.Price.create(
            unit_amount=payment.payment_amount,
            currency="usd",
            recurring={"interval": "month"},
            product=product.id,
        )
        pay = stripe.checkout.Session.create(
            success_url="https://example.com/success",
            line_items=[
                {
                    "price": price,
                    "quantity": 1,
                },
            ],
            mode="subscription",
        )
        get_url = stripe.checkout.Session.retrieve(pay.last_response.data['id'],)
        print(get_url.url)
        return get_url.url


class PaymentsDestroyView(generics.DestroyAPIView):
    """
    Представление для удаления платежа
    """
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializers



