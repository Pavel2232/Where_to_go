from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description_short = HTMLField(max_length=500, verbose_name="Краткое Описание")
    description_long = HTMLField(max_length=5000, verbose_name="Полное описание")
    lng = models.FloatField(verbose_name="Долгота")
    lat = models.FloatField(verbose_name="Широта")

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.title


class ImageNumber(models.IntegerChoices):
    first = 1, "Первая"
    second = 2, "Вторая"


class Image(models.Model):
    imgs = models.ImageField(upload_to='django_media/', verbose_name="Изображение")
    places = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name="Локация", related_name="image")
    number_image = models.IntegerField(choices=ImageNumber.choices, default=ImageNumber.first,
                                       verbose_name="Номер фотографии", blank=True, null=True, db_index=True)

    class Meta:
        ordering = ['number_image']
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return f"{self.number_image} {self.places.title}"
