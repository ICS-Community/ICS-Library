# Generated by Django 4.0.4 on 2022-05-24 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_tag_text_tag_title_alter_tag_tid'),
        ('forum', '0005_rename_t_content_content_content_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='kind',
        ),
        migrations.AddField(
            model_name='content',
            name='tags',
            field=models.ManyToManyField(to='tags.tag', verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='content',
            name='content',
            field=models.CharField(max_length=3000, verbose_name='正文'),
        ),
        migrations.AlterField(
            model_name='content',
            name='intro',
            field=models.CharField(max_length=256, verbose_name='内容摘要'),
        ),
        migrations.AlterField(
            model_name='content',
            name='t_id',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='指向内容的id'),
        ),
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(max_length=64, verbose_name='标题'),
        ),
    ]
