# Generated by Django 2.2.9 on 2020-02-27 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0004_remove_card_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='buy.Order'),
        ),
    ]
