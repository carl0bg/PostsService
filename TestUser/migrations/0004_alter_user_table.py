# Generated by Django 5.1 on 2024-09-14 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestUser', '0003_user_delete_testuser'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]