# Generated by Django 5.0.6 on 2024-06-26 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musician', '0003_rename_musicianmodel_musician'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='phone_no',
            field=models.CharField(max_length=11),
        ),
    ]
