# Generated by Django 5.1 on 2024-08-21 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_posts_text_alter_posts_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='document',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='posts',
            name='text',
            field=models.TextField(blank=True, verbose_name='Текст поста'),
        ),
    ]
