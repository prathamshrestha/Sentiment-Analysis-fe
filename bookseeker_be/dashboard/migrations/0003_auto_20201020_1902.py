# Generated by Django 3.1.1 on 2020-10-20 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20201019_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_model',
            name='bio',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
