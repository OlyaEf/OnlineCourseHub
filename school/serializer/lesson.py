from rest_framework import serializers

from school.models.lesson import Lesson
from school.serializer.course import CourseSerializer


class LessonSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True)

    class Meta:
        model = Lesson
        fields = '__all__'

