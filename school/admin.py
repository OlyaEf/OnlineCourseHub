from django.contrib import admin

from school.models.course import Course
from school.models.lesson import Lesson

admin.site.register(Course)
admin.site.register(Lesson)

