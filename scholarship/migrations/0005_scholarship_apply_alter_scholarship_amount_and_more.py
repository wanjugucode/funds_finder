# Generated by Django 5.0.3 on 2024-03-13 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0004_alter_scholarship_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarship',
            name='apply',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='amount',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]