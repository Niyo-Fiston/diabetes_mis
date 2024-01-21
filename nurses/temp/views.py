from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import NurseRegistrationForm, AdminLoginForm

def nurse_registration(request):
    if request.method == 'POST':
        form = NurseRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_nurse = True
            user.save()
            return redirect('login')
    else:
        form = NurseRegistrationForm()
    return render(request, 'nurse_registration.html', {'form': form})

def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user and user.is_admin:
                login(request, user)
                return redirect('admin_dashboard')  # Change this to your admin dashboard URL
    else:
        form = AdminLoginForm()
    return render(request, 'admin_login.html', {'form': form})
