# Generated by Django 3.1.6 on 2021-02-19 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funapp', '0008_auto_20210219_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]