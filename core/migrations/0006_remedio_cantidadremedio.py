# Generated by Django 3.2.3 on 2022-05-05 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220505_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='remedio',
            name='cantidadRemedio',
            field=models.CharField(default=0, max_length=15, verbose_name='Cantidad de remedio en gr o mg'),
            preserve_default=False,
        ),
    ]
