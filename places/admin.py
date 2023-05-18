from django.contrib import admin
from django.contrib.admin import register

from places.models import Place, Image

class ImageInline(admin.TabularInline):
    model = Image
@register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


# Register your models here.
# admin.site.register(Place)
admin.site.register(Image)

