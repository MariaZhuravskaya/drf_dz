from django.core.management import BaseCommand

from payments.models import Payments
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        u1 = User.objects.get(pk=1)
        u2 = User.objects.get(pk=2)
        payments_list = [
            {'user': u1, 'date': '2023-10-20', 'payment_amount': '10000', 'payment_method': 'перевод', 'payment_course_lesson': 'курс'},
            {'user': u2, 'date': '2023-10-20', 'payment_amount': '25000', 'payment_method': 'наличные', 'payment_course_lesson': 'курс'},

        ]

        payments_create = []
        for payments_item in payments_list:
            payments_create.append(
                Payments(**payments_item)
            )

        Payments.objects.bulk_create(payments_create)
