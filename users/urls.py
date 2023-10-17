from django.urls import path

from users.views import UserListView, UserRetrieveView, UserCreateView, UserUpdateView, UserDestroyView

urlpatterns = [
    path('', UserListView.as_view()),
    path('<int:pk>', UserRetrieveView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('update/<int:pk>', UserUpdateView.as_view()),
    path('delete/<int:pk>', UserDestroyView.as_view()),
]
