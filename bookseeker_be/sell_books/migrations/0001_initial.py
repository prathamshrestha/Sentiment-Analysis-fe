# Generated by Django 3.1.1 on 2020-10-09 08:34

from django.db import migrations, models
import sell_books.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booksell_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('bookpicture', models.ImageField(blank=True, upload_to=sell_books.models.upload_path)),
                ('age', models.IntegerField(blank=True)),
                ('description', models.CharField(max_length=500)),
                ('status', models.DateField(blank=True)),
            ],
        ),
    ]