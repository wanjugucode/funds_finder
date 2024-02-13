# Generated by Django 5.0.2 on 2024-02-13 12:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0011_alter_bookmark_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarshipapplication',
            name='approved_scholarship',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applyscholarship', to='scholarships.approvedscholarship'),
        ),
    ]