# Generated by Django 3.1.3 on 2020-12-27 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project0', '0002_auto_20201207_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='image',
        ),
    ]