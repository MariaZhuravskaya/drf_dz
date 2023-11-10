from rest_framework import serializers
from stripe import PaymentIntent

from payments.models import Payments


class PaymentsSerializers(serializers.ModelSerializer):
    """
    Сериализатор для представления платежа
    """
    pay = PaymentIntent.stripe_id

    class Meta:
        model = Payments
        fields = '__all__'
