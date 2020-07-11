from django import forms


class ChannelForm(forms.Form):
    channel_name = forms.CharField(max_length=50, label='channel')


class CommentForm(forms.Form):
    text = forms.CharField(label='text', max_length=300)


class NewVideoForm(forms.Form):
    title = forms.CharField(label='Title', max_length=20)
    description = forms.CharField(label='Description', max_length=300)
    file = forms.FileField()
