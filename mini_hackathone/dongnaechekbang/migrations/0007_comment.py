# Generated by Django 3.0.6 on 2020-07-31 13:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dongnaechekbang', '0006_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment_contents', models.CharField(max_length=200)),
                ('comment_writer', models.CharField(max_length=100)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='dongnaechekbang.Blog')),
            ],
        ),
    ]
