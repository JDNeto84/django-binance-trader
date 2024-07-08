from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from core.domain.repositories import UserRepository
from core.domain.services import AuthenticationService, BinanceService
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

user_repository = UserRepository()
auth_service = AuthenticationService(user_repository)
binance_service = BinanceService(user_repository)

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
        if auth_service.register_user(username, password, email):
            return redirect('login')
        return render(request, 'auth/register.html', {'error': 'User registration failed'})

@method_decorator(login_required, name='dispatch')
class UpdateKeysView(View):
    def get(self, request):
        return render(request, 'profile/profile_form.html')
    
    def post(self, request):
        api_key = request.POST['api_key']
        secret_key = request.POST['secret_key']
        if auth_service.update_user_keys(request.user.username, api_key, secret_key):
            return redirect('profile')
        return render(request, 'profile/profile_form.html', {'error': 'Failed to update keys'})

@method_decorator(login_required, name='dispatch')
class UserBalancesView(View):
    def get(self, request):
        try:
            balances = binance_service.get_user_balances(request.user.username)
            return render(request, 'balances/balances.html', {'balances': balances})
        except Exception as e:
            return render(request, 'balances/balances.html', {'error': str(e)})

@method_decorator(login_required, name='dispatch')
class UserBalancesPartialView(View):
    def get(self, request):
        try:
            balances = binance_service.get_user_balances(request.user.username)
            return render(request, 'balances/partials/balances_list.html', {'balances': balances})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@method_decorator(login_required, name='dispatch')
class CreateMarketOrderView(View):
    def post(self, request):
        try:
            symbol = request.POST.get('symbol')
            side = request.POST.get('side')
            quantity = float(request.POST.get('quantity'))
            order = binance_service.create_market_order(request.user.username, symbol, side, quantity)
            return JsonResponse(order)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

def home(request):
    return render(request, 'index.html')

@login_required
def profile_view(request):
    return render(request, 'profile/profile.html', {'user': request.user})

@login_required
def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html', {'user': request.user})
