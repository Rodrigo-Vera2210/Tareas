# Generated by Django 5.0.4 on 2024-04-16 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarea', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tarea',
            options={'verbose_name': 'Tarea', 'verbose_name_plural': 'Tareas'},
        ),
        migrations.AlterField(
            model_name='tarea',
            name='nombre',
            field=models.CharField(default=' ', max_length=255),
        ),
    ]
