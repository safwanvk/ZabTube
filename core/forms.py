from django import forms


class ChannelForm(forms.Form):
    channel_name = forms.CharField(max_length=50, label='channel')