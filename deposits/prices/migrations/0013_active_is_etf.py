# Generated by Django 2.2.19 on 2022-08-30 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0012_active_avg_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='active',
            name='is_etf',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
