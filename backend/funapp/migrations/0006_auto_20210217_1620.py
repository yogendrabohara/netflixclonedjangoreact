# Generated by Django 3.1.6 on 2021-02-18 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funapp', '0005_auto_20210217_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='image_path',
            field=models.FileField(upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
