# Generated by Django 5.0.2 on 2024-03-15 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0003_recipe_author_recipe_created_on_recipe_updated_on_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
