# Generated by Django 2.2.9 on 2020-02-27 11:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0005_card_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buy.Order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default=1, max_length=1000),
        ),
        migrations.AlterField(
            model_name='order',
            name='aphone',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='district',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='thana',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
