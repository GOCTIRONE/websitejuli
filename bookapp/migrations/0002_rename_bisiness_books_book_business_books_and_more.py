# Generated by Django 4.1.3 on 2022-11-12 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book", old_name="bisiness_books", new_name="business_books",
        ),
        migrations.AlterField(
            model_name="book",
            name="category",
            field=models.ManyToManyField(related_name="books", to="bookapp.category"),
        ),
    ]