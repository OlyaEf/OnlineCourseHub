from rest_framework import serializers

from school.models.lesson import Lesson
from school.serializer.course import CourseSerializer
from school.validators import ValidateYoutubeLinks


class LessonSerializer(serializers.ModelSerializer):
    # courses = CourseSerializer(many=True)
    validators = [ValidateYoutubeLinks(field='video_url')]

    class Meta:
        model = Lesson
        fields = '__all__'

