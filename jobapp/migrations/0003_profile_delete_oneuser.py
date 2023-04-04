# Generated by Django 4.1.7 on 2023-04-04 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0002_oneuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=15)),
                ('domain', models.CharField(max_length=20)),
                ('about', models.TextField(max_length=25)),
                ('email', models.EmailField(max_length=20)),
                ('profile', models.ImageField(blank=True, null=True, upload_to='article_images/')),
                ('cv_upload', models.FileField(blank=True, null=True, upload_to='article_images/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Oneuser',
        ),
    ]
