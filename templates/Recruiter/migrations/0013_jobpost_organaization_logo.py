# Generated by Django 4.2.1 on 2023-06-07 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recruiter', '0012_alter_jobpost_job_brief'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='organaization_logo',
            field=models.ImageField(blank=True, default='jobpost.png', null=True, upload_to=''),
        ),
    ]
