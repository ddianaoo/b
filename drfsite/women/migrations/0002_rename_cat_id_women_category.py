# Generated by Django 4.2.11 on 2024-03-15 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='women',
            old_name='cat_id',
            new_name='category',
        ),
    ]
