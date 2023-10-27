from rest_framework import serializers

from subscription.models import Subscription


class SubscriptionSerializers(serializers.ModelSerializer):
    """
    Сериализатор для представления подписки
    """
    class Meta:
        model = Subscription
        fields = '__all__'
