# Generated by Django 2.2.19 on 2022-08-30 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0013_active_is_etf'),
    ]

    operations = [
        migrations.AddField(
            model_name='active',
            name='is_money',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
