# Generated by Django 4.1 on 2022-10-10 07:44

import blogcalc.yandex_s3_storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blogger_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogger',
            name='avatar',
            field=models.ImageField(blank=True, help_text='Upload your profile avatar. Max size - 1 mb', null=True, storage=blogcalc.yandex_s3_storage.UsersAvatarsStorage(), upload_to=''),
        ),
    ]