# Generated by Django 2.2.19 on 2022-08-08 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0008_auto_20220809_0157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='active',
            name='date_of_sell',
        ),
        migrations.RemoveField(
            model_name='active',
            name='price_of_sell',
        ),
    ]
