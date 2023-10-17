from rest_framework import serializers

from lesson.models import Lesson, Well


class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class WellSerializers(serializers.ModelSerializer):
    class Meta:
        model = Well
        fields = '__all__'
