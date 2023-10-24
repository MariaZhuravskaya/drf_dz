from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from lesson.models import Lesson, Course
from lesson.permissions import IsModerator
from lesson.serializers import LessonSerializers, CourseSerializers


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    permission_classes = [IsAuthenticated, IsModerator]


class LessonListView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticated]


class LessonRetrieveView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticated]


class LessonCreateView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsModerator]


class LessonUpdateView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticated]


class LessonDestroyView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticated, IsModerator]
