# Generated by Django 4.0.4 on 2022-05-27 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0004_remove_bookshelf_b_id_remove_bookshelf_f_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='u_id',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]