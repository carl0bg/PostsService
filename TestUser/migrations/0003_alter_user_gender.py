# Generated by Django 5.1 on 2024-11-02 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestUser', '0002_user_bio_user_birthday_user_gender_user_github'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=6),
        ),
    ]
