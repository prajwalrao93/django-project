# Generated by Django 4.1.7 on 2023-02-27 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vidstr', '0021_remove_posts_comments_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]
