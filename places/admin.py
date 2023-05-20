from adminsortable2.admin import SortableAdminMixin, SortableStackedInline, SortableTabularInline, SortableAdminBase
from django.contrib import admin
from django.contrib.admin import register
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from places.models import Place, Image
from django.urls import reverse

class ImageInline(SortableStackedInline):
    model = Image
    readonly_fields = ['image_link']
    fields = ('imgs', 'image_link','number_image')
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
class PlaceAdmin(SortableAdminBase,admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]




# Register your models here.
# admin.site.register(Place)
admin.site.register(Image)

