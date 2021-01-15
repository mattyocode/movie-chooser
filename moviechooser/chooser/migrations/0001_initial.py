# Generated by Django 3.1.4 on 2021-01-14 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(choices=[(1, 'Mystery'), (2, 'Sci-Fi'), (3, 'Thriller'), (4, 'Biography'), (5, 'Drama'), (6, 'History'), (7, 'War'), (8, 'Crime'), (9, 'Action'), (10, 'Comedy'), (11, 'Horror'), (12, 'Adventure'), (13, 'Romance'), (14, 'Family'), (15, 'Fantasy'), (16, 'Animation')], max_length=20)),
            ],
        ),
    ]