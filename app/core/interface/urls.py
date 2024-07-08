from django.contrib import admin
from django.urls import path
from core.interface.views import UserBalancesView, UserBalancesPartialView, CreateMarketOrderView, home, profile_view, dashboard_view, LoginView, LogoutView, RegisterView, UpdateKeysView

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', profile_view, name='profile'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('update-keys/', UpdateKeysView.as_view(), name='update_keys'),
    path('balances/', UserBalancesView.as_view(), name='balances'),
    path('balances/partial/', UserBalancesPartialView.as_view(), name='user_balances_partial'),
    path('order/create/', CreateMarketOrderView.as_view(), name='create_market_order'),
]
