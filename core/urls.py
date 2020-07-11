from django.urls import path

from core.views import ChannelView

urlpatterns = [

    path('<user>/channel', ChannelView.as_view())
]