# Generated by Django 3.0.6 on 2020-07-04 03:07

from django.db import migrations, models
import myapp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20200627_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author_comment',
            field=models.CharField(max_length=60, validators=[myapp.validators.validate_author_comment]),
        ),
    ]
