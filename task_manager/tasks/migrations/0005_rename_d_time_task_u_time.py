# Generated by Django 4.2.5 on 2023-09-23 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20230923_1922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='d_time',
            new_name='u_time',
        ),
    ]