# Generated by Django 4.1.3 on 2022-11-18 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bookapp", "0014_rename_stock_book_juli"),
    ]

    operations = [
        migrations.RemoveField(model_name="book", name="juli",),
    ]
