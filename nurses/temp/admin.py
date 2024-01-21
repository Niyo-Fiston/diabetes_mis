from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Nurse, Admin

class NurseInline(admin.StackedInline):
    model = Nurse
    can_delete = False
    verbose_name_plural = 'Nurse'

class CustomUserAdmin(UserAdmin):
    inlines = (NurseInline, )

admin.site.register(CustomUser, CustomUserAdmin)
