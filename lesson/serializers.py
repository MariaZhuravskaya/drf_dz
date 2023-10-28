from rest_framework import serializers

from lesson.models import Lesson, Course, Subscription
from lesson.validators import URLValidator


class LessonSerializers(serializers.ModelSerializer):
    """
    Сериализатор для представления урока
    """
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [URLValidator(fields='video')]


class SubscriptionSerializers(serializers.ModelSerializer):
    """
    Сериализатор для представления подписки
    """
    class Meta:
        model = Subscription
        fields = '__all__'


class CourseSerializers(serializers.ModelSerializer):
    """
    Сериализатор для представления курса
    """
    lesson_count = serializers.SerializerMethodField()
    lesson = serializers.SerializerMethodField()
    subscription = SubscriptionSerializers(source='subscription_set', read_only=True, many=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'img', 'lesson_count', 'lesson', 'subscription')

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()

    def get_lesson(self, course):
        return LessonSerializers(Lesson.objects.filter(course=course), many=True).data



