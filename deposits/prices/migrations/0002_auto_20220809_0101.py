# Generated by Django 2.2.19 on 2022-08-08 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'Счет'},
        ),
        migrations.AlterModelOptions(
            name='active',
            options={'ordering': ['-date_of_buy'], 'verbose_name': 'Актив'},
        ),
    ]
