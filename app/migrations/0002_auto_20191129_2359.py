# Generated by Django 2.2.4 on 2019-11-29 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='delete_yn',
            field=models.CharField(default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='postmemory',
            name='delete_yn',
            field=models.CharField(default='N', max_length=1),
        ),
    ]
