# Generated by Django 4.2.1 on 2023-05-15 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_image_number_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='places',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='places.place', verbose_name='Локация'),
        ),
    ]
