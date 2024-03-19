from django.urls import path
from rest_framework import routers

from users.apps import UsersConfig
from users.views import PaymentListView, UserUpdateView, UserDetailView

app_name = UsersConfig.name

urlpatterns = [
    path('user/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('payment/', PaymentListView.as_view(), name='payment_list'),

]

"""router = routers.SimpleRouter()
router.register('users', UserDetailView)

urlpatterns += router.urls"""
