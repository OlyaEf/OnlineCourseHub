from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from school.models.course import Course, CourseSubscription
from school.models.lesson import Lesson
from school.permissions import IsOwner, IsModerator
from school.serializer.course import CourseSerializer, CourseSubscriptionSerializer
from school.serializer.lesson import LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsOwner | IsModerator]   # Применяем разрешения


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    # permission_classes = [IsOwner]  # Применяем разрешения
    permission_classes = [AllowAny]  # Применяем разрешения


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsModerator]  # Применяем разрешения


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsModerator]  # Применяем разрешения


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsModerator]  # Применяем разрешения


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]  # Применяем разрешения


class CourseSubscribeAPIView(generics.CreateAPIView):
    serializer_class = CourseSubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Course.objects.all()

    def create(self, request, *args, **kwargs):
        course = self.get_object()  # Получаем объект курса из URL
        user = request.user

        # Проверяем не подписан ли пользователь уже на этот курс
        if CourseSubscription.objects.filter(user=user, course=course).exists():
            return Response({"detail": "Вы уже подписаны на этот курс."}, status=status.HTTP_400_BAD_REQUEST)
        # Создаем подписку
        subscription = CourseSubscription(user=user, course=course)
        subscription.save()

        return Response({"detail": "Подписка успешно установлена."}, status=status.HTTP_201_CREATED)


class CourseUnsubscribeAPIView(generics.DestroyAPIView):
    serializer_class = CourseSubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return CourseSubscription.objects.filter(user=user, is_active=True)

    def perform_destroy(self, instance):
        # Устанавливаем подписку как неактивную вместо фактического удаления
        instance.is_active = False
        instance.save()
