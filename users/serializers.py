from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from payments.models import Payments
from users.models import User


class UserSerializers(serializers.ModelSerializer):
    """
    Сериализатор для представления пользователя
    """
    payments = serializers.SerializerMethodField()

    def get_payments(self, obj_user):
        payments = Payments.objects.filter(user=obj_user)
        return [(p.payment_amount, p.payment_method, p.date) for p in payments]

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'city', 'payments']




