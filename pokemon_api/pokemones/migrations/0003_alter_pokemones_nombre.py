# Generated by Django 4.0 on 2021-12-17 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemones', '0002_pokemones_icono_alter_pokemones_imagen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemones',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
