import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from lesson.models import Lesson, Course, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        """Подготовка данных перед каждым тестом"""
        self.client = APIClient()
        self.user = User.objects.create(email='test@gmail.com', password='123qwe456rty')
        self.client.force_authenticate(user=self.user)  # Аутентифицируем клиента с созданным пользователем
        self.user.save()

        self.course = Course.objects.create(
            name='TEST',
            description='TEST'
        )
        self.course.save()

        self.lesson = Lesson.objects.create(
            name='TEST',
            description='TEST',
            video='https://www.youtube.com/watch?v=1HtEPEn4-LY',
        )

    def test_create_lesson(self):
        """тестирование создания урока"""
        data = {
            'name': self.lesson.name,
            'description': self.lesson.description,
            'course': self.course.id,
            'video': self.lesson.video
        }

        response = self.client.post(
            '/lesson/create/',
            data=data
        )

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 13)

    def test_list_lesson(self):
        """тестирование вывода списка уроков"""

        response = self.client.get(
            reverse('lesson:lesson_list'),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {'count': 12,
             'next': 'http://testserver/lesson/?page=2',
             'previous': None,
             'results': [{'active': True,
                          'course': 1,
                          'description': 'высший пилотаж',
                          'id': 1,
                          'img': None,
                          'name': 'урок 3 Django DRF',
                          'owner': None,
                          'video': None},
                         {'active': True,
                          'course': 1,
                          'description': 'высший пилотаж',
                          'id': 2,
                          'img': None,
                          'name': 'урок 20 Django DRF Permission',
                          'owner': None,
                          'video': None},
                         {'active': True,
                          'course': 1,
                          'description': 'высший пилотаж',
                          'id': 3,
                          'img': None,
                          'name': 'урок 20 DRF Permission',
                          'owner': None,
                          'video': None},
                         {'active': True,
                          'course': 1,
                          'description': 'пилотаж',
                          'id': 4,
                          'img': None,
                          'name': 'урок 150 DRF Permission',
                          'owner': None,
                          'video': None},
                         {'active': True,
                          'course': 1,
                          'description': 'пилотаж',
                          'id': 5,
                          'img': None,
                          'name': 'урок 150 DRF Permission',
                          'owner': None,
                          'video': None},
                         {'active': True,
                          'course': 1,
                          'description': 'пилотаж',
                          'id': 6,
                          'img': None,
                          'name': 'урок 150 DRF Permission',
                          'owner': None,
                          'video': None},
                         {'active': True,
                          'course': 1,
                          'description': 'http://my.sky.pro/',
                          'id': 7,
                          'img': None,
                          'name': 'урок 150 DRF Permission',
                          'owner': None,
                          'video': None},
                         {'active': True,
                          'course': 1,
                          'description': 'http://my.sky.pro/',
                          'id': 8,
                          'img': None,
                          'name': 'урок 150 DRF Permission',
                          'owner': None,
                          'video': None},
                         {'active': True,
                          'course': 1,
                          'description': 'http://my.sky.pro/',
                          'id': 9,
                          'img': None,
                          'name': 'http://my.sky.pro/',
                          'owner': None,
                          'video': None},
                         {'active': True,
                          'course': 1,
                          'description': 'http://my.sky.pro/',
                          'id': 10,
                          'img': None,
                          'name': 'http://my.sky.pro/',
                          'owner': None,
                          'video': None}]}
        )

    def test_delete_lesson(self):
        """тестирование удаления урока"""

        response = self.client.delete(
            '/lesson/delete/' + str(self.lesson.id)
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def tearDown(self):
        User.objects.all().delete()
        Lesson.objects.all().delete()
        Course.objects.all().delete()


class SubscriptionTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='user@test.com', password='test')
        self.client.force_authenticate(user=self.user)  # Аутентифицируем клиента с созданным пользователем
        self.user.set_password('1q2w3e4r')
        self.user.save()

        self.course = Course.objects.create(
            name='Course Subscription',
            description='Course Subscription'
        )
        self.course.save()

        self.subscription = Subscription.objects.create(
            course=self.course,
            user=self.user,
        )

    def test_create_subscription(self):
        """тестирование создания подписки"""

        data = {
            "course": self.course.id,
            "user": self.user.id,
        }

        response = self.client.post(
            '/lesson/subscription/create/',
            data=data
        )
        print(response.json())

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subscription.objects.all().count(), 3)

    def test_delete_subscription(self):
        """тестирование удаления подписки"""

        response = self.client.delete(
            '/lesson/subscription/delete/' + str(self.subscription.id),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

