# Generated by Django 3.2.15 on 2022-09-13 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0003_remove_book_book_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_publication',
        ),
        migrations.AlterField(
            model_name='book',
            name='book_author',
            field=models.CharField(max_length=75),
        ),
    ]
