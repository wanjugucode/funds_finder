# Generated by Django 5.0.2 on 2024-02-14 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0013_bookmark_userprofile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='user',
        ),
        migrations.RemoveField(
            model_name='scholarshipapplication',
            name='user',
        ),
    ]