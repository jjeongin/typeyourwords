# Generated by Django 3.1.3 on 2021-01-03 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project0', '0003_remove_word_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='image',
            field=models.ImageField(null=True, upload_to='outputs/'),
        ),
    ]
