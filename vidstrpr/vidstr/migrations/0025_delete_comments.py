# Generated by Django 4.1.7 on 2023-02-27 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vidstr', '0024_rename_post_id_comments_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]