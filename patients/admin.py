from django.contrib import admin

# Register your models here.
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'glucose_level', 'weight', 'height')
    search_fields = ('first_name', 'last_name', 'age', 'glucose_level', 'weight', 'height')

admin.site.register(Patient, PatientAdmin)
admin.site.site_header = 'Biryogo Diabetes Administration'
admin.site.site_title = 'Biryogo Diabetes Admin'
admin.site.index_title = 'Welcome to Biryogo Diabetes Administration'