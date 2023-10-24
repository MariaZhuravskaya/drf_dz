from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter

from payments.models import Payments
from payments.serializers import PaymentsSerializers


class PaymentsListView(generics.ListAPIView):
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


class PaymentsDestroyView(generics.DestroyAPIView):
    """
    Представление для удаления платежа
    """
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializers

