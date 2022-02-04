"""tic_toc_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import CreateGameView, JoinGameView, GameStateView

urlpatterns = [
    path('game/create-new', CreateGameView.as_view({'post': 'create'}), name='create new game'),
    path('game/join', JoinGameView.as_view({'put': 'update'}), name='join to new game'),
    
    # # ******** question?? I also can use this way of handing data in get API. is it secure??? *******
    # path(
    #     "instruments/<str:symbol>/",
    #     GetAnInstrument.as_view({"get": "retrieve"}),
    #     name="get-an-instrument",
    # )
    # def retrieve(self, *args, **kwargs):
    #     instrument_symbol = kwargs.get("symbol", None)
    path('game/status', GameStateView.as_view({'get': 'retrieve'}), name='get game status')
]
