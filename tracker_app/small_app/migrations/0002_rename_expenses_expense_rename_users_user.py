# Generated by Django 5.1 on 2024-08-29 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('small_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Expenses',
            new_name='Expense',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
