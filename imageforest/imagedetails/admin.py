# from django.contrib import admin

# Register your models here.

# from .models import Image

# admin.site.register(Image)

from django.contrib import admin
from .models import image

class imageAdmin(admin.ModelAdmin):
    list_display = ["title","description", "image"]

admin.site.register(image, imageAdmin)  