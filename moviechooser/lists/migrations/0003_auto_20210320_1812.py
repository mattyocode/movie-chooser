# Generated by Django 3.1.4 on 2021-03-20 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20210319_1340'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-watched', '-date_added']},
        ),
    ]