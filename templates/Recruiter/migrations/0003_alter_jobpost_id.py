# Generated by Django 4.2.1 on 2023-06-06 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recruiter', '0002_alter_jobpost_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
