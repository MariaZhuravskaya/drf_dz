from django.urls import path

from payments.views import PaymentsListView, PaymentsRetrieveView, PaymentsCreateView, PaymentsDestroyView

urlpatterns = [
    path('list/', PaymentsListView.as_view(), name='payments_list'),
    path('retrieve/<int:pk>', PaymentsRetrieveView.as_view(), name='payments_retrieve'),
    path('create/', PaymentsCreateView.as_view(), name='payments_create'),
    path('delete/<int:pk>', PaymentsDestroyView.as_view(), name='payments_delete'),
]
