# Generated by Django 3.2.9 on 2021-11-09 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0003_auto_20211108_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='jersey_number',
            field=models.IntegerField(),
        ),
    ]
