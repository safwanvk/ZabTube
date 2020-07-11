from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from core.models import Video, Channel


class ChannelView(View):
    template_name = "channel_view.html"

    def get(self, request, user):
        if request.user.is_authenticated:
            videos = Video.objects.filter(user__username=user).order_by("-datetime")
            channel = Channel.objects.filter(user__username=user).get()
            context = {'videos': videos,
                       'channel': channel}
        return render(request, self.template_name, context)