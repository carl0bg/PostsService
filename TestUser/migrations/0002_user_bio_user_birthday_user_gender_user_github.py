# Generated by Django 5.1 on 2024-11-02 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestUser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=6),
        ),
        migrations.AddField(
            model_name='user',
            name='github',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
