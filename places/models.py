from django.db import models

# Create your models here.

class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description_short = models.CharField(max_length=500,verbose_name="Короткое описание")
    description_long = models.CharField(max_length=5000,verbose_name="Полное описание")
    lng = models.FloatField(verbose_name="Долгота")
    lat = models.FloatField(verbose_name="Широта")


    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.title

