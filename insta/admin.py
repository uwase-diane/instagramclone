from django.contrib import admin
from .models import Image, Profile, Comments, Follow

admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Follow)
admin.site.register(Comments)