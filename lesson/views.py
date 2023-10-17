from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from lesson.models import Lesson, Well
from lesson.serializers import LessonSerializers, WellSerializers


class WellViewSet(ModelViewSet):
    queryset = Well.objects.all()
    serializer_class = WellSerializers


class LessonListView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers


class LessonRetrieveView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers


class LessonCreateView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers


class LessonUpdateView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers


class LessonDestroyView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
