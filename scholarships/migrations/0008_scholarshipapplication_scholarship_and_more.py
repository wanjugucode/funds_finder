# Generated by Django 5.0.2 on 2024-02-12 09:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0007_alter_scholarshipapplication_id_approvedscholarship'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarshipapplication',
            name='scholarship',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='scholarships.scholarships'),
        ),
        migrations.AlterField(
            model_name='approvedscholarship',
            name='approval_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='scholarshipapplication',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='scholarshipapplication',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='scholarshipapplication',
            name='essay',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='scholarshipapplication',
            name='is_approved',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='scholarshipapplication',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='scholarships',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]