# Generated by Django 4.0.4 on 2022-05-12 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_delete_producto_remedio_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remedio',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]