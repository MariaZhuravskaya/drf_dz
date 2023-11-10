from django.urls import path

from payments.views import PaymentsListView, PaymentsRetrieveView, PaymentsCreateView, PaymentsDestroyView, \
    GetPaymentView

urlpatterns = [
    path('list/', PaymentsListView.as_view(), name='payments_list'),
    path('retrieve/<int:pk>', PaymentsRetrieveView.as_view(), name='payments_retrieve'),
    path('create/', PaymentsCreateView.as_view(), name='payments_create'),
    path('payment/<str:payment_id>/', GetPaymentView.as_view(), name='payment_get'),
    path('delete/<int:pk>', PaymentsDestroyView.as_view(), name='payments_delete'),

]
