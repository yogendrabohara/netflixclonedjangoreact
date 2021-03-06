# Generated by Django 3.1.6 on 2021-02-17 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funapp', '0002_auto_20210216_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180)),
                ('link', models.EmailField(max_length=180)),
                ('description', models.CharField(max_length=180)),
                ('created_at', models.DateTimeField()),
                ('category_id', models.SmallIntegerField()),
                ('image_path', models.FilePathField(verbose_name='')),
            ],
        ),
    ]
