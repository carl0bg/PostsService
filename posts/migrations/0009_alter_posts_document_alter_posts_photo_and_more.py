# Generated by Django 5.1 on 2024-08-21 10:32

import storages.backends.s3
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_posts_photo_posts_video_alter_posts_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='document',
            field=models.FileField(blank=True, null=True, storage=storages.backends.s3.S3Storage(location='documentdjango'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='posts',
            name='photo',
            field=models.ImageField(blank=True, null=True, storage=storages.backends.s3.S3Storage(location='photodjango'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='posts',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Текст поста'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='video',
            field=models.FileField(blank=True, null=True, storage=storages.backends.s3.S3Storage(location='videodjango'), upload_to=''),
        ),
    ]
