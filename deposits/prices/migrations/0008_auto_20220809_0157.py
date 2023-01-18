# Generated by Django 2.2.19 on 2022-08-08 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0007_active_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='active',
            old_name='result',
            new_name='result_percent',
        ),
        migrations.AddField(
            model_name='active',
            name='result_rouble',
            field=models.FloatField(blank=True, null=True),
        ),
    ]