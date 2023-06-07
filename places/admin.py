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

    def get_image_display(self, obj: Image):
        try:
            url = obj.imgs.url
            height = 200
            return format_html('<img src = {url} height={height}/>', url=url, height=height)
        except Exception as e:
            print(e)

    get_image_display.short_description = 'Превью'


@register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    """Модель place с подключенной image"""
    inlines = [
        ImageInline,
    ]


admin.site.register(Image)
