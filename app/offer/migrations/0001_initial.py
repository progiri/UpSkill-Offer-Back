# Generated by Django 3.2 on 2021-04-15 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='title')),
                ('salary', models.PositiveIntegerField(default=0, verbose_name='salary')),
                ('org', models.CharField(max_length=60, verbose_name='organization')),
                ('addr', models.CharField(max_length=60, verbose_name='address')),
                ('desc', models.TextField(verbose_name='描述')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
            ],
            options={
                'verbose_name': 'offer',
                'verbose_name_plural': 'offer',
                'db_table': 'offer',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=60, verbose_name='full name')),
                ('github', models.URLField(verbose_name='github link')),
                ('phone', models.CharField(max_length=20, verbose_name='phone number')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
            ],
            options={
                'verbose_name': 'resume',
                'verbose_name_plural': 'resume',
                'db_table': 'resume',
            },
        ),
    ]