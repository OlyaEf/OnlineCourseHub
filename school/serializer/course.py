from rest_framework import serializers

from school.models.course import Course
from school.models.lesson import Lesson


class CourseSerializer(serializers.ModelSerializer):
    lessons = serializers.PrimaryKeyRelatedField(queryset=Lesson.objects.all(), many=True)
    lessons_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_count(self, obj):
        return obj.lessons.count()
