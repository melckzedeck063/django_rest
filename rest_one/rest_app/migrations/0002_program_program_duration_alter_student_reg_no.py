# Generated by Django 5.1.2 on 2024-10-14 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='program_duration',
            field=models.CharField(default='3 yrs', max_length=6),
        ),
        migrations.AlterField(
            model_name='student',
            name='reg_no',
            field=models.CharField(max_length=15),
        ),
    ]
