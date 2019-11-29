import datetime
from django.db import models


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    content = models.CharField(max_length=5000)
    delete_yn = models.CharField(max_length=1, default='N')
    create_at = models.DateField(default=datetime.datetime.now())
    update_at = models.DateField(blank=True, null=True)
    delete_at = models.DateField(blank=True, null=True)

    class Meta():
        db_table = 'tbl_post'


class PostMemory(models.Model):
    id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    kanji = models.CharField(max_length=255)
    hiragana = models.CharField(max_length=255)
    hangul = models.CharField(max_length=255)
    delete_yn = models.CharField(max_length=1, default='N')
    create_at = models.DateField(default=datetime.datetime.now())
    update_at = models.DateField(blank=True, null=True)
    delete_at = models.DateField(blank=True, null=True)

    class Meta():
        db_table = 'tbl_post_memory'

        