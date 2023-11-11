from django.conf import settings
from django.core.mail import send_mail
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from lesson.models import Lesson, Course, Subscription
from lesson.paginators import LessonPagination, CoursePagination
from lesson.permissions import IsModerator, IsOwner, IsNotModerator
from lesson.serializers import LessonSerializers, CourseSerializers, SubscriptionSerializers
from lesson.tasks import send_mail_update_course


class CourseViewSet(ModelViewSet):
    """
    Представление для CRUD курса
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    pagination_class = CoursePagination

    def get(self, request):
        """
        Метод пагинации вывода курсов
        :param request: paginated_queryset - метод для разбиения queryset
        :return: get_paginated_response - возврат ответа со страницей данных и информацией о пагинации
        """
        queryset = Course.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = CourseSerializers(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def get_permissions(self):
        """
        Метод по предоставлению прав доступа
        :return:
        """
        if self.request.method in ['CREATE', 'DELETE', 'UPDATE']:
            self.permission_classes = [IsOwner, IsNotModerator]
        else:
            self.permission_classes = [IsOwner]
        return super(CourseViewSet, self).get_permissions()

    def perform_create(self, serializer):
        """
        Метод сохранения пользователя при создании урока
        :param serializer:
        :return:
        """
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()
        return super().perform_create(serializer)


class CourseUpdateView(generics.UpdateAPIView):
    """
    Представление для изменения курса
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

    @classmethod
    def send_mailing(cls, email):
        send_mail(
            subject=f'Обновление курса',
            message='Курс, на который вы подписаны обновился. Предлагаем посмотреть обновление на нашем сайте .',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )

    def perform_update(self, serializer):
        serializer.save()
        email = serializer.context['request'].user
        self.send_mailing(email)

        send_mail_update_course.delay(email)
        # result.successful()
        print(f"рассылка на обновление отправлена на {email}")


class LessonListView(generics.ListAPIView):
    """
    Представление для просмотра списка уроков
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    pagination_class = LessonPagination
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonRetrieveView(generics.RetrieveAPIView):
    """
    Представление для просмотра урока
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsOwner]


class LessonCreateView(generics.CreateAPIView):
    """
    Представление для создания урока
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticated | IsNotModerator]

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


class LessonUpdateView(generics.UpdateAPIView):
    """
    Представление для изменения урока
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsOwner]


class LessonDestroyView(generics.DestroyAPIView):
    """
    Представление для удаления урока
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsOwner]


class SubscriptionCreateView(generics.CreateAPIView):
    """
    Представление для создания подписки
    """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializers


class SubscriptionUpdateView(generics.UpdateAPIView):
    """
    Представление для обновления подписки
    """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializers


class SubscriptionListView(generics.ListAPIView):
    """
    Представление для просмотра списка подписок
    """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializers


class SubscriptionDestroyView(generics.DestroyAPIView):
    """
    Представление для удаления подписки
    """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializers
