import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import game.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tic_toc_back.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            game.routing.websocket_urlpatterns
        )
    ),
    # Just HTTP for now. (We can add other protocols later.)
})





# import os

# import django
# from channels.http import AsgiHandler
# from channels.routing import ProtocolTypeRouter,get_default_application


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tic_toc_back.settings')
# django.setup()


# application=get_default_application()
