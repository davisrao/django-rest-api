# Generated by Django 3.2.9 on 2021-11-09 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_auto_20211108_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='first_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='player',
            name='jersey_number',
            field=models.IntegerField(max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='last_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
