# Generated by Django 3.2.3 on 2022-05-07 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remedio_cantidadremedio'),
    ]

    operations = [
        migrations.AddField(
            model_name='remedio',
            name='imagenRemedio',
            field=models.ImageField(default=0, upload_to='', verbose_name='Imagen del remedio'),
            preserve_default=False,
        ),
    ]