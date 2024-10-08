# Generated by Django 5.1 on 2024-09-03 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('small_app', '0002_rename_expenses_expense_rename_users_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telephone', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('budgetmonthly', models.DecimalField(decimal_places=2, max_digits=10)),
                ('source_of_income', models.CharField(max_length=100)),
                ('other_sources', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='small_app.user')),
            ],
        ),
    ]
