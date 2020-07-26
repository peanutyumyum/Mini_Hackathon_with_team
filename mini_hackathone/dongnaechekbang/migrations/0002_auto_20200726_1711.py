# Generated by Django 3.0.6 on 2020-07-26 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dongnaechekbang', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('city', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='evaluation_about_bookstore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation', models.IntegerField(default=0)),
                ('comment_about_bookstore_with_text', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='bookstore',
            name='city_address_of_bookstore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dongnaechekbang.city'),
        ),
    ]
