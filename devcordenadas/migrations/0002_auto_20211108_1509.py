# Generated by Django 3.2.9 on 2021-11-08 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devcordenadas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'usuario', 'verbose_name_plural': 'usuarios'},
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]