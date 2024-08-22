# Generated by Django 5.1 on 2024-08-21 10:28

import storages.backends.s3
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_posts_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='photo',
            field=models.ImageField(null=True, storage=storages.backends.s3.S3Storage(location='photodjango'), upload_to=''),
        ),
        migrations.AddField(
            model_name='posts',
            name='video',
            field=models.FileField(null=True, storage=storages.backends.s3.S3Storage(location='videodjango'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='posts',
            name='document',
            field=models.FileField(null=True, storage=storages.backends.s3.S3Storage(location='documentdjango'), upload_to=''),
        ),
    ]