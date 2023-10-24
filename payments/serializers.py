from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from payments.models import Payments
from users.serializers import UserSerializers


class PaymentsSerializers(serializers.ModelSerializer):
    """
    Сериализатор для представления платежа
    """

    class Meta:
        model = Payments
        fields = '__all__'


