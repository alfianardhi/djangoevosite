# Generated by Django 3.0.6 on 2020-06-27 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
