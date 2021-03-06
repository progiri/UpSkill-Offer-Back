# Generated by Django 3.2 on 2021-04-15 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='target_offer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='offer.offer', verbose_name='target offer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='offer',
            name='desc',
            field=models.TextField(verbose_name='description'),
        ),
    ]
