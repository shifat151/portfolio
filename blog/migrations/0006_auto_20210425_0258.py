# Generated by Django 3.2 on 2021-04-24 20:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='body',
        ),
        migrations.AddField(
            model_name='blog',
            name='description',
            field=ckeditor.fields.RichTextField(default='The sky is red', verbose_name='Job Description'),
            preserve_default=False,
        ),
    ]
