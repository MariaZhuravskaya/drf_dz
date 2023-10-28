from django.urls import path
from rest_framework import routers

from lesson.apps import LessonConfig
from lesson.views import LessonListView, LessonRetrieveView, LessonCreateView, LessonUpdateView, LessonDestroyView, \
    CourseViewSet, SubscriptionCreateView, SubscriptionDestroyView, CourseUpdateView

router = routers.DefaultRouter()
router.register(r'course', CourseViewSet)

app_name = LessonConfig.name

urlpatterns = [
    path('', LessonListView.as_view(), name='lesson_list'),
    path('<int:pk>', LessonRetrieveView.as_view(), name='lesson_retrieve'),
    path('create/', LessonCreateView.as_view(), name='lesson_create'),
    path('update/<int:pk>', LessonUpdateView.as_view(), name='lesson_update'),
    path('delete/<int:pk>', LessonDestroyView.as_view(), name='lesson_delete'),

    path('course/update/<int:pk>', CourseUpdateView.as_view()),
    path('subscription/create/', SubscriptionCreateView.as_view()),
    path('subscription/delete/<int:pk>', SubscriptionDestroyView.as_view(), name='subscription_delete'),
]+router.urls
