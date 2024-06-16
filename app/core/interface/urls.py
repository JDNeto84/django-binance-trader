from django.contrib import admin
from django.urls import path
from core.interface.views import home

urlpatterns = [
    path('', home, name='home'),
    path('info/', home, name='home'),  
    path('admin/', admin.site.urls),
]
