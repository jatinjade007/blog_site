# Generated by Django 4.2.2 on 2023-06-11 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Content',
            fields=[
                ('blog_content_id', models.IntegerField(primary_key=True, serialize=False)),
                ('blog_content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('blog_id', models.IntegerField(primary_key=True, serialize=False)),
                ('blog_title', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('blog_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog_content')),
            ],
        ),
        migrations.AddField(
            model_name='blog_content',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogs'),
        ),
    ]