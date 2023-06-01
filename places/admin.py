from adminsortable2.admin import SortableStackedInline, SortableAdminBase
from django.contrib import admin
from django.contrib.admin import register
from django.utils.safestring import mark_safe
from places.models import Place, Image


class ImageInline(SortableStackedInline):
    """Добавления изображения в админ-панели"""
    model = Image
    readonly_fields = ['image_link']
    fields = ('imgs', 'image_link', 'number_image')

    def image_link(self, obj):
        try:
            return mark_safe('<img src = "{url}" width= "{width}" height={height} />'.format(
                url=obj.imgs.url,
                width=200,
                height=200,
            )
            )

        except Exception as e:
            print(e)

    image_link.short_description = "Превью"


@register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    """Модель place с подключенной image"""
    inlines = [
        ImageInline,
    ]


admin.site.register(Image)
