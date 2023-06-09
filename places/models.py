from django.db import models
from django.db.models import TextField
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description_short = TextField(verbose_name='Краткое Описание', null=True, blank=True)
    description_long = HTMLField(verbose_name='Полное описание', null=True, blank=True)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.title



class Image(models.Model):
    imgs = models.ImageField(upload_to='django_media/', verbose_name='Изображение')
    places = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Локация', related_name='images')
    number_image = models.IntegerField(default=1,
                                       verbose_name='Номер фотографии',
                                       blank=True,
                                       db_index=True)

    class Meta:
        ordering = ['number_image']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f'{self.number_image} {self.places.title}'
