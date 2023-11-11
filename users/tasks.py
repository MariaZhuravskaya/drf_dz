from datetime import datetime

from celery import shared_task
from django.conf import settings

from users.models import User


@shared_task
def is_active_false():
    users = User.objects.all()
    today = datetime.today()
    for user in users:
        delta = today.date() - user.last_login.date()
        if delta.days > 30:
            user.is_active = False
            user.save()
            print("Пользователь, заходил более 30 дней назад, теперь он неактивен")
        else:
            print("Пользователь активен")



