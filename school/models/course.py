from django.db import models

from constants import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='course')
    preview = models.ImageField(verbose_name='preview', **NULLABLE)
    description = models.TextField(verbose_name='description')
    lessons = models.ManyToManyField('Lesson')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return (f'{self.name}'
                f'{self.description}')

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'



