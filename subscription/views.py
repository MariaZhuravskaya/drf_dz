from django.shortcuts import render
from rest_framework import generics

from subscription.models import Subscription
from subscription.serializers import SubscriptionSerializers


class SubscriptionCreateView(generics.CreateAPIView):
    """
    Представление для создания урока
    """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializers


    def perform_create(self, serializer):
        """
        Сохранение пользователя при создании урока
        :param serializer:
        :return:
        """
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()
        return super().perform_create(serializer)
