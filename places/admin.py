from adminsortable2.admin import SortableStackedInline, SortableAdminBase
from django.contrib import admin
from django.contrib.admin import register
from django.utils.html import format_html
from places.models import Place, Image


class ImageInline(SortableStackedInline):
    """Добавления изображения в админ-панели"""
    model = Image
    readonly_fields = ['get_image_display']
    fields = ('imgs', 'get_image_display', 'number_image')

    def get_image_display(self, image: Image):
        url = image.img.url
        height = 200
        return format_html('<img src = {url} height={height}/>', url=url, height=height)

    get_image_display.short_description = 'Превью'


@register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    """Модель place с подключенной image"""
    inlines = [
        ImageInline,
    ]


admin.site.register(Image)
