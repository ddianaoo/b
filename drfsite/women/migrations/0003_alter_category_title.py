# Generated by Django 4.2.11 on 2024-03-15 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_rename_cat_id_women_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
    ]
