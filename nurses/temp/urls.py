from django.urls import path
from .views import nurse_registration, admin_login

urlpatterns = [
    path('nurse-registration/', nurse_registration, name='nurse_registration'),
    path('admin-login/', admin_login, name='admin_login'),
]
