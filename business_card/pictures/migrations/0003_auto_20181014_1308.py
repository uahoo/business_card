# Generated by Django 2.1.1 on 2018-10-14 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0002_auto_20181014_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='img',
            field=models.ImageField(upload_to='pictures'),
        ),
    ]
