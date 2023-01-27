# Generated by Django 3.1.4 on 2023-01-27 12:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_remove_delfin_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atributo_delfin',
            name='valor',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-2), django.core.validators.MaxValueValidator(2)]),
        ),
    ]
