from rest_framework import serializers

from payments.models import Payments


class PaymentsSerializers(serializers.ModelSerializer):
    """
    Сериализатор для представления платежа
    """

    class Meta:
        model = Payments
        fields = '__all__'
