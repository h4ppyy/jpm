# Generated by Django 2.2.4 on 2019-11-29 15:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20191130_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2019, 11, 30, 0, 21, 0, 348573)),
        ),
        migrations.AlterField(
            model_name='postmemory',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2019, 11, 30, 0, 21, 0, 348573)),
        ),
    ]
