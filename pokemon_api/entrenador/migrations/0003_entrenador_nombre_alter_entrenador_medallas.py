# Generated by Django 4.0 on 2021-12-17 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrenador', '0002_alter_entrenador_fecharegistro'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrenador',
            name='nombre',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='entrenador',
            name='medallas',
            field=models.IntegerField(default=0),
        ),
    ]
