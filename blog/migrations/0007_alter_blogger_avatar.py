# Generated by Django 4.1 on 2022-09-27 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment_blog_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogger',
            name='avatar',
            field=models.ImageField(blank=True, help_text='Upload your profile avatar', null=True, upload_to='images/avatars'),
        ),
    ]
