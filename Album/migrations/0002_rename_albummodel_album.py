# Generated by Django 5.0.6 on 2024-06-26 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Album', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AlbumModel',
            new_name='Album',
        ),
    ]