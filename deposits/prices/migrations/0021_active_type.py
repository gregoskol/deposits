# Generated by Django 2.2.19 on 2022-09-08 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0020_active_sum_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='active',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='active_type', to='prices.ActiveType'),
        ),
    ]