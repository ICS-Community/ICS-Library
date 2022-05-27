# Generated by Django 4.0.4 on 2022-05-27 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0008_gsentence'),
        ('users', '0005_alter_profile_u_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='B_bookshelf',
            new_name='BookForBS',
        ),
        migrations.AlterField(
            model_name='profile',
            name='u_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户ID'),
        ),
    ]
