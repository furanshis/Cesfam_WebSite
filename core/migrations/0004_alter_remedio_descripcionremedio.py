# Generated by Django 3.2.3 on 2022-05-05 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remedio_precioremedio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remedio',
            name='descripcionRemedio',
            field=models.CharField(max_length=300, verbose_name='Descripción del remedio'),
        ),
    ]
