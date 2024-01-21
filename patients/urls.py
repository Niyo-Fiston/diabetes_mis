# patients/urls.py

from django.urls import path
from .views import patient_list, add_patient, delete_patient, update_patient
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', patient_list, name='patient_list'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('add/', add_patient, name='add_patient'),
    path('delete/<int:patient_id>/', delete_patient, name='delete_patient'),
    path('update/<int:patient_id>/', update_patient, name='update_patient'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
]
