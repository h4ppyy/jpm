# Generated by Django 2.2.4 on 2019-11-29 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191130_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2019, 11, 30, 0, 3, 19, 253443)),
        ),
        migrations.AlterField(
            model_name='postmemory',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2019, 11, 30, 0, 3, 19, 254471)),
        ),
    ]