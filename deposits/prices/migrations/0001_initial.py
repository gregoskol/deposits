# Generated by Django 2.2.19 on 2022-08-08 21:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Active',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=200)),
                ('date_of_buy', models.DateTimeField()),
                ('price_of_buy', models.FloatField()),
                ('amount', models.IntegerField()),
                ('date_of_sell', models.DateTimeField()),
                ('price_of_sell', models.FloatField()),
                ('is_block', models.BooleanField()),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='active', to='prices.Account')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='active', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
