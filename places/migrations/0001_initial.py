# Generated by Django 4.2.1 on 2023-05-15 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('imgs', models.ImageField(upload_to='django_media/')),
                ('description_short', models.CharField(max_length=500)),
                ('description_long', models.CharField(max_length=1000)),
                ('lng', models.FloatField()),
                ('lat', models.FloatField()),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
            },
        ),
    ]
