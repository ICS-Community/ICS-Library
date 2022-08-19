# Generated by Django 3.2.5 on 2022-08-18 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_integral'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='integral',
            new_name='points',
        ),
        migrations.AddField(
            model_name='status',
            name='check_in_points',
            field=models.IntegerField(default=0, verbose_name='签到获取的积分'),
        ),
        migrations.AlterField(
            model_name='status',
            name='check_in_time',
            field=models.DateField(blank=True, null=True, verbose_name='最后签到日期'),
        ),
    ]