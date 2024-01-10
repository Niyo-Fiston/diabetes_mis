# patients/urls.py

from django.urls import path
from .views import patient_list, add_patient, delete_patient

urlpatterns = [
    path('', patient_list, name='patient_list'),
    path('add/', add_patient, name='add_patient'),
    path('delete/<int:patient_id>/', delete_patient, name='delete_patient'),
]