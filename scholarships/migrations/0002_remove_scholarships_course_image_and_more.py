# Generated by Django 5.0.1 on 2024-01-29 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scholarships',
            name='course_image',
        ),
        migrations.RemoveField(
            model_name='scholarships',
            name='expiry_date',
        ),
        migrations.RemoveField(
            model_name='scholarships',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='scholarships',
            name='time',
        ),
        migrations.RemoveField(
            model_name='scholarships',
            name='title',
        ),
        migrations.AddField(
            model_name='scholarships',
            name='application_deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scholarships',
            name='award_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='scholarships',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scholarships',
            name='eligibility_criteria',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scholarships',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='scholarships',
            name='organization',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='scholarships',
            name='scholarship_type',
            field=models.CharField(blank=True, choices=[('merit', 'Merit-Based'), ('need', 'Need-Based')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='scholarships',
            name='status',
            field=models.CharField(blank=True, choices=[('open', 'Open'), ('closed', 'Closed'), ('ongoing', 'Ongoing')], max_length=50, null=True),
        ),
    ]
