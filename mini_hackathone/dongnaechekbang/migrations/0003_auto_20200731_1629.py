# Generated by Django 3.0.7 on 2020-07-31 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dongnaechekbang', '0002_bookstore_bookstore_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookstore',
            old_name='bookstore_image',
            new_name='bookstore_image1',
        ),
        migrations.AddField(
            model_name='bookstore',
            name='bookstore_image2',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
        migrations.AddField(
            model_name='bookstore',
            name='bookstore_image3',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
        migrations.AddField(
            model_name='bookstore',
            name='bookstore_image4',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
    ]