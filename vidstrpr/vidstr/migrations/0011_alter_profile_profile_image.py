# Generated by Django 4.1.7 on 2023-02-22 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vidstr', '0010_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='default_profile_pic.png', upload_to='profile_pics/'),
        ),
    ]
