# Generated by Django 5.0 on 2023-12-08 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_rename_likes_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]