# Generated by Django 4.1 on 2022-09-07 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_post',
            name='like_dislikes',
        ),
        migrations.RemoveField(
            model_name='likes_dislikes',
            name='likes_dislike_status',
        ),
    ]
