#from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patients/', include('patients.urls')),
    path('nurses/', include('nurses.urls')),
]
