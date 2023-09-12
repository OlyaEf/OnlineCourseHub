from django.db import models

from constants import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='course')
    preview = models.ImageField(verbose_name='preview', **NULLABLE)
    description = models.TextField(verbose_name='description')

    def __str__(self):
        return (f'{self.name}'
                f'{self.description}')

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='lesson')
    preview = models.ImageField(verbose_name='preview', **NULLABLE)
    description = models.TextField(verbose_name='description')
    video_url = models.URLField(verbose_name='video URL', **NULLABLE)

    def __str__(self):
        return (f'{self.name}'
                f'{self.description}')

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
