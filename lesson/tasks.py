from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_mail_update_course(email):
    send_mail(
        subject='Обновление курса',
        message='Курс, на который вы подписаны обновился. Предлагаем посмотреть обновление',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
    print("Отложенное уведомление отправлено")


