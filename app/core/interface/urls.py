from django.contrib import admin
from django.urls import path
from core.interface.views import home
from core.interface.views import profile_view, dashboard_view, LoginView, LogoutView, RegisterView

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', profile_view, name='profile'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
