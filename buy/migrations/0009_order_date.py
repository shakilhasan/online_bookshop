# Generated by Django 2.2.10 on 2020-03-01 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0008_auto_20200227_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
