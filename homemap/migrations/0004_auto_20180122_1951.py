# Generated by Django 2.0.1 on 2018-01-22 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homemap', '0003_auto_20180122_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantinfo',
            name='website',
            field=models.URLField(max_length=500),
        ),
    ]
