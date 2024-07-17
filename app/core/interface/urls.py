from django.contrib import admin
from django.urls import path
from core.interface.views import CheckInputOrder, home, monitor, profile_view, dashboard_view, LoginView, LogoutView, RegisterView, UpdateKeysView, UserOrdersView, UserBalancesView, UserBalancesPartialView, CreateMarketOrderView

urlpatterns = [
    path('', home, name='home'),    
    path('admin/', admin.site.urls),
    path('monitor/', monitor, name='monitor'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', profile_view, name='profile'),
    path('balances/', UserBalancesView.as_view(), name='balances'),
    path('orders/', UserOrdersView.as_view(), name='orders'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('update-keys/', UpdateKeysView.as_view(), name='update_keys'),
    path('balances/partial/', UserBalancesPartialView.as_view(), name='user_balances_partial'),
    path('order/create/', CreateMarketOrderView.as_view(), name='create_market_order'),
    path('check_input_order/', CheckInputOrder, name="check_input_order"),
    
]
