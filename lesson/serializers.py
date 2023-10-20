from rest_framework import serializers

from lesson.models import Lesson, Course


class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializers(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lesson = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ('name', 'description', 'img', 'lesson_count', 'lesson')

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()

    def get_lesson(self, course):
        return LessonSerializers(Lesson.objects.filter(course=course), many=True).data
