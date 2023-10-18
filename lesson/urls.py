from django.urls import path
from rest_framework import routers

from lesson.views import LessonListView, LessonRetrieveView, LessonCreateView, LessonUpdateView, LessonDestroyView, \
    CourseViewSet

router = routers.DefaultRouter()
router.register(r'course', CourseViewSet)

urlpatterns = [
    path('', LessonListView.as_view()),
    path('<int:pk>', LessonRetrieveView.as_view()),
    path('create/', LessonCreateView.as_view()),
    path('update/<int:pk>', LessonUpdateView.as_view()),
    path('delete/<int:pk>', LessonDestroyView.as_view()),
]+router.urls
