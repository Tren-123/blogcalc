# Generated by Django 4.1 on 2022-09-19 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_likes_dislikes_like_dislike_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='blog_post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.blog_post'),
            preserve_default=False,
        ),
    ]
