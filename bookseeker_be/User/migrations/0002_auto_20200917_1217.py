# Generated by Django 2.1 on 2020-09-17 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='createusers',
            options={},
        ),
        migrations.AlterModelManagers(
            name='createusers',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='createusers',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='createusers',
            name='user_permissions',
        ),
    ]
