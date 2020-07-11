from django.contrib import admin

# Register your models here.
from core.models import Video, Comment, Channel

admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Channel)