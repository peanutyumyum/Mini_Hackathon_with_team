# Generated by Django 3.0.6 on 2020-07-31 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dongnaechekbang', '0002_auto_20200731_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.TextField(),
        ),
    ]
