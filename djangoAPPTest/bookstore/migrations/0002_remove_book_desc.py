# Generated by Django 2.2.20 on 2021-05-12 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='desc',
        ),
    ]
