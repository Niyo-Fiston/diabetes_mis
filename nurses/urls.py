# nurses/urls.py

from django.urls import path
from .views import nurse_list, add_nurse, delete_nurse

urlpatterns = [
    path('', nurse_list, name='nurse_list'),
    path('add/', add_nurse, name='add_nurse'),
    path('delete/<int:nurse_id>/', delete_nurse, name='delete_nurse'),
]
