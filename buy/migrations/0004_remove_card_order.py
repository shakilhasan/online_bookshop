# Generated by Django 2.2.9 on 2020-02-27 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0003_card_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='order',
        ),
    ]
