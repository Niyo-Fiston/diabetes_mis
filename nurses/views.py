from django.shortcuts import render, redirect

# Create your views here.
# nurses/views.py
from .models import Nurse
from .forms import NurseForm

def nurse_list(request):
    nurses = Nurse.objects.all()
    return render(request, 'nurses/nurse_list.html', {'nurses': nurses})

def add_nurse(request):
    if request.method == 'POST':
        form = NurseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nurse_list')
    else:
        form = NurseForm()
    
    return render(request, 'nurses/add_nurse.html', {'form': form})

def delete_nurse(request, nurse_id):
    nurse = Nurse.objects.get(id=nurse_id)
    nurse.delete()
    return redirect('nurse_list')
