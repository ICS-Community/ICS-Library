# Generated by Django 4.0.4 on 2022-05-24 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_remove_content_kind_content_tags_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='intro',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='内容摘要'),
        ),
    ]
