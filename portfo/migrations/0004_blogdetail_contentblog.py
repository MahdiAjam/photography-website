# Generated by Django 5.1.3 on 2024-12-17 10:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfo', '0003_category_portfoliodetail_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/blog/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='portfo.category')),
            ],
        ),
        migrations.CreateModel(
            name='ContentBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(choices=[('text', 'text'), ('image', 'image')], max_length=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/blog/')),
                ('order', models.PositiveIntegerField()),
                ('blog_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='portfo.blogdetail')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
