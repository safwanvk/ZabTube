from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from core.forms import ChannelForm
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


class CreateChannelView(View):
    template_name = "channel_create.html"

    def get(self, request):
        if request.user.is_authenticated:
            try:
                if Channel.objects.filter(user__username=request.user).get().channel_name != "":
                    return HttpResponseRedirect('/')
            except Channel.DoesNotExist:
                form = ChannelForm()
                channel = False
                return render(request, self.template_name, {'form': form, 'channel': channel})

    def post(self, request):
        # pass filled out HTML-Form from View to RegisterForm()
        form = ChannelForm(request.POST)
        if form.is_valid():
            # create a User account
            print(form.cleaned_data['channel_name'])
            channel_name = form.cleaned_data['channel_name']
            user = request.user
            subscribers = 0
            new_channel = Channel(channel_name=channel_name, user=user, subscribers=subscribers)
            new_channel.save()
            return HttpResponseRedirect('/')
        return HttpResponse('This is Register view. POST Request.')