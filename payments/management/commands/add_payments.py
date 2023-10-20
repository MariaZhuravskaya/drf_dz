from django.core.management import BaseCommand

from lesson.models import Course, Lesson
from payments.models import Payments
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        u1 = User.objects.get(pk=1)
        u2 = User.objects.get(pk=2)
        n_course = range(0, len(Course.objects.all()))
        n_lesson = range(0, len(Lesson.objects.all()))
        for i in n_course:
            course = Course.objects.all()[i]
            for j in n_lesson:
                lesson = Lesson.objects.all()[j]

                payments_list = [
                    {'user': u1, 'date': '2023-10-20', 'payment_amount': '55000', 'payment_method': 'перевод', 'payment_course': course},
                    {'user': u2, 'date': '2023-10-20', 'payment_amount': '125000', 'payment_method': 'наличные', 'payment_lesson': lesson},

                ]

                payments_create = []
                for payments_item in payments_list:
                    payments_create.append(
                        Payments(**payments_item)
                    )

                Payments.objects.bulk_create(payments_create)
