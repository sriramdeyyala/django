# Generated by Django 4.0.6 on 2022-07-28 07:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('read_by', models.CharField(max_length=50)),
                ('read_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]