from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from lesson.models import Lesson, Course
from lesson.permissions import IsModerator, IsOwner, IsNotModerator
from lesson.serializers import LessonSerializers, CourseSerializers


class CourseViewSet(ModelViewSet):
    """
    Представление для CRUD курса
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

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


class LessonListView(generics.ListAPIView):
    """
    Представление для просмотра списка уроков
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
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
    permission_classes = [IsNotModerator | IsOwner]
