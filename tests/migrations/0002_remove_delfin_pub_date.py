# Generated by Django 3.1.4 on 2023-01-27 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delfin',
            name='pub_date',
        ),
    ]
