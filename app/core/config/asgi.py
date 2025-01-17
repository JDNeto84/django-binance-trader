import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import core.infrastructure.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.config.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            core.infrastructure.routing.websocket_urlpatterns
        )
    ),
})
