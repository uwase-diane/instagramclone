from django.contrib import admin
from .models import Image, Profile, Comment, Follow

admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Follow)
admin.site.register(Comment)