# Generated by Django 3.1.3 on 2021-01-16 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project0', '0005_auto_20210116_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='img_h',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='img_w',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
