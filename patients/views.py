from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient
from .forms import PatientForm, PatientSearchForm, UpdatePatientForm, RegisterForm
from django.db import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate



@login_required(login_url="/login")
def patient_list(request):
    patients = Patient.objects.all()
    search_form = PatientSearchForm(request.GET)
    if search_form.is_valid():
        search_query = search_form.cleaned_data.get('search_query', '')
        patients = patients.filter(
            models.Q(first_name__icontains=search_query) |
            models.Q(last_name__icontains=search_query) |
            models.Q(address__icontains=search_query) |
            models.Q(age__icontains=search_query) |
            models.Q(address__icontains=search_query) |
            models.Q(glucose_level__icontains=search_query) |
            models.Q(treatment_plan__icontains=search_query) |
            models.Q(weight__icontains=search_query) |
            models.Q(height__icontains=search_query) 
        )

        return render(request, 'patients/patient_list.html', {'patients': patients, 'search_form': search_form})
    
    else:
        return render(request, 'patients/patient_list.html', {'patients': patients})

@login_required(login_url="/login")
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    
    return render(request, 'patients/add_patient.html', {'form': form})

@login_required(login_url="/login")
def delete_patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    patient.delete()
    return redirect('patient_list')

@login_required(login_url="/login")
def update_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    
    if request.method == 'POST':
        form = UpdatePatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')  # Redirect to your patient list view
    else:
        form = UpdatePatientForm(instance=patient)

    return render(request, 'patients/update_patient.html', {'form': form, 'patient': patient})

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('patient_list')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})