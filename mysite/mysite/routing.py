from channels.auth import AuthMiddlewareStack # type: ignore
from channels.routing import ProtocolTypeRouter, URLRouter # type: ignore
import chat.routing # type: ignore

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})