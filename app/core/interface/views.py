from django.shortcuts import render, redirect
from django.views import View
from core.domain.repositories import UserRepository
from core.domain.services import AuthenticationService
from django.contrib.auth.decorators import login_required

user_repository = UserRepository()
auth_service = AuthenticationService(user_repository)

class LoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        if auth_service.login_user(request, username, password):
            return redirect('profile')
        return render(request, 'auth/login.html', {'error': 'Invalid credentials'})

class LogoutView(View):
    def get(self, request):
        auth_service.logout_user(request)
        return redirect('login')

class RegisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if user := auth_service.register_user(username, password, email):
            return redirect('login')
        return render(request, 'auth/register.html', {'error': 'User registration failed'})

def home(request):
    return render(request, 'index.html')

@login_required
def profile_view(request):
    return render(request, 'profile/profile.html', {'user': request.user})

@login_required
def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html', {'user': request.user})
