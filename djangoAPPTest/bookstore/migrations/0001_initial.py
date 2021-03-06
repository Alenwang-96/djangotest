# Generated by Django 2.2.20 on 2021-05-12 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='书名')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('desc', models.CharField(default='This is a good book', max_length=200)),
            ],
        ),
    ]
