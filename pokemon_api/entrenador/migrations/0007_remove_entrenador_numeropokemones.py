# Generated by Django 4.0 on 2021-12-18 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrenador', '0006_alter_entrenadorpokemones_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrenador',
            name='numeroPokemones',
        ),
    ]
