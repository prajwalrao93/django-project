# Generated by Django 4.1.7 on 2023-02-22 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vidstr', '0003_alter_posts_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='images',
            field=models.ImageField(upload_to='uploaded/'),
        ),
    ]
