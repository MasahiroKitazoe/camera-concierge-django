# Generated by Django 2.1.3 on 2018-12-23 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0002_auto_20181223_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='url',
            field=models.TextField(),
        ),
    ]
