from rest_framework import serializers

from lesson.models import Lesson, Course
from lesson.validators import URLValidator


class LessonSerializers(serializers.ModelSerializer):
    """
    Сериализатор для представления урока
    """
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [URLValidator(fields='video')]


class CourseSerializers(serializers.ModelSerializer):
    """
    Сериализатор для представления курса
    """
    lesson_count = serializers.SerializerMethodField()
    lesson = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'img', 'lesson_count', 'lesson')

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()

    def get_lesson(self, course):
        return LessonSerializers(Lesson.objects.filter(course=course), many=True).data
