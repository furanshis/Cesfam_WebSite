# Generated by Django 3.2.3 on 2022-05-04 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_categoriaremedio_remedio'),
    ]

    operations = [
        migrations.AddField(
            model_name='remedio',
            name='precioRemedio',
            field=models.IntegerField(default=0, verbose_name='Precio del remedio'),
            preserve_default=False,
        ),
    ]