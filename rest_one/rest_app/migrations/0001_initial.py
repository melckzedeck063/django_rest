# Generated by Django 5.1.2 on 2024-10-14 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(max_length=100)),
                ('program_code', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'program',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=10)),
                ('phone_number', models.CharField(max_length=14)),
                ('reg_no', models.CharField(max_length=10)),
                ('registered', models.BooleanField(default=False)),
                ('yos', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_app.program')),
            ],
            options={
                'db_table': 'student',
                'ordering': ['first_name'],
            },
        ),
    ]
