# Generated by Django 3.1.3 on 2021-01-16 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project0', '0004_word_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='img_h',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='word',
            name='img_w',
            field=models.IntegerField(null=True),
        ),
    ]
