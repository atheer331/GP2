# Generated by Django 4.2.1 on 2023-05-13 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_alter_seeker_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seeker',
            name='profile_image',
            field=models.ImageField(blank=True, default='user-default.png', null=True, upload_to=''),
        ),
    ]
