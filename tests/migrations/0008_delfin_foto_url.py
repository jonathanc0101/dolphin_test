# Generated by Django 3.1.4 on 2023-01-30 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0007_auto_20230128_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='delfin',
            name='foto_url',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
