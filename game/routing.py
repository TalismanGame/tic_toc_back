from channels.routing import ProtocolTypeRouter

application = ProtocolTypeRouter({
    'websocket':AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
            
            path('whole1/',PracticeConsumer())
            ])
        )
    )
})

# application = ProtocolTypeRouter({

# })