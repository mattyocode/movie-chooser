# Generated by Django 3.1.4 on 2021-03-19 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-date_added']},
        ),
    ]
