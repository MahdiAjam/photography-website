# Generated by Django 5.1.3 on 2024-12-17 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfo', '0005_remove_blogdetail_tags_blogdetail_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentblog',
            name='content_type',
        ),
    ]