# Generated by Django 4.1.7 on 2023-03-01 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vidstr', '0029_rename_body_comment_comment_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='like_status',
            field=models.BooleanField(default=True),
        ),
    ]