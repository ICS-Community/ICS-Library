# Generated by Django 3.2.5 on 2022-08-17 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='integral',
            field=models.BigIntegerField(default=0, verbose_name='积分'),
        ),
    ]