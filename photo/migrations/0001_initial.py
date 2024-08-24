# Generated by Django 5.1 on 2024-08-24 11:31

import django.db.models.deletion
import posts.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(blank=True, null=True, storage=posts.storage.PhotoStorage(), upload_to='')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='posts.posts')),
            ],
        ),
    ]
