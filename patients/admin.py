from django.contrib import admin

# Register your models here.
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'glucose_level', 'weight', 'height')
    search_fields = ('first_name', 'last_name', 'age', 'glucose_level', 'weight', 'height')

admin.site.register(Patient, PatientAdmin)