# Generated by Django 2.2.19 on 2022-09-07 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0017_auto_20220907_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='active',
            name='actual_price',
        ),
        migrations.RemoveField(
            model_name='active',
            name='result_percent',
        ),
        migrations.RemoveField(
            model_name='active',
            name='result_rouble',
        ),
    ]
