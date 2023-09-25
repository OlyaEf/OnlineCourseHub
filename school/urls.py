from django.urls import path

from school.apps import SchoolConfig
from rest_framework.routers import DefaultRouter

from school.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, CourseSubscribeAPIView, CourseUnsubscribeAPIView

app_name = SchoolConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-destroy'),

    path('courses/<int:pk>/subscribe/', CourseSubscribeAPIView.as_view(), name='course-subscribe'),
    path('courses/<int:pk>/unsubscribe/', CourseUnsubscribeAPIView.as_view(), name='course-unsubscribe'),
] + router.urls

