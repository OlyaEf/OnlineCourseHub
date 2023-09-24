from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from school.models.lesson import Lesson
from users.models import User  # Импортируйте модель User, если она находится в users.models


class LessonTestCase(APITestCase):
    def setUp(self):
        # Тестовый пользователь
        self.user = User.objects.create(
            email='test@example.com',
            password='testpassword',
        )
        # Аутентифицируйте пользователя
        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        # URL для создания урока
        url = reverse('lesson-create')

        # Данные урока, которые будут отправлены в POST-запросе
        lesson_data = {
            'name': 'Test Lesson',
            'preview': None,
            'description': 'This is a test lesson.',
            'video_url': 'https://youtube.com',
            'courses': [],
            'owner': self.user.id,  # ID владельца урока
        }

        response = self.client.post(url, lesson_data, format='json')

        # Проверка статуса ответа (ожидаем статус 201 CREATED)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Проверка создания урока в базе данных
        self.assertTrue(Lesson.objects.filter(name='Test Lesson').exists())
