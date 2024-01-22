from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # ... other URL patterns
    path('admin/', admin.site.urls),
    path('', include('patients.urls')),
    path('', include('django.contrib.auth.urls')),
    
]


