# Generated by Django 3.1.1 on 2020-10-15 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sell_books', '0002_auto_20201015_1341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booksell_model',
            old_name='name',
            new_name='bookname',
        ),
    ]
