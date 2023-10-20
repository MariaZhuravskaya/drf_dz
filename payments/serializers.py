from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from payments.models import Payments
from users.serializers import UserSerializers


class PaymentsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'


