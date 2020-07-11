from django import forms


class ChannelForm(forms.Form):
    channel_name = forms.CharField(max_length=50, label='channel')


class CommentForm(forms.Form):
    text = forms.CharField(label='text', max_length=300)
