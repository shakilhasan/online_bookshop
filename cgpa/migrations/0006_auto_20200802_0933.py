# Generated by Django 2.2.10 on 2020-08-02 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cgpa', '0005_course_result_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='course',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cgpa.Course'),
        ),
    ]