# Generated by Django 4.0 on 2021-12-18 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entrenador', '0009_artificial_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrenadorarticialpokemones',
            name='entrenador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrenador.artificial'),
        ),
    ]
