# Generated by Django 2.2.10 on 2020-03-01 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0009_order_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'get_latest_by': ['id']},
        ),
    ]