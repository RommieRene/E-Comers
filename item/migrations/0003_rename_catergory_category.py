# Generated by Django 5.2.1 on 2025-05-14 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_rename_item_catergory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catergory',
            new_name='Category',
        ),
    ]
