# Generated by Django 2.2.19 on 2022-08-11 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0010_auto_20220811_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='active',
            name='actual_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]