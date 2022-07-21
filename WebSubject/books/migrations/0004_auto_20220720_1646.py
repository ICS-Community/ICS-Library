# Generated by Django 3.2.5 on 2022-07-20 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_rename_book_starts_b_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='starts',
            name='stars1',
            field=models.BigIntegerField(blank=True, default=0, verbose_name='一星评价'),
        ),
        migrations.AlterField(
            model_name='starts',
            name='stars2',
            field=models.BigIntegerField(blank=True, default=0, verbose_name='二星评价'),
        ),
        migrations.AlterField(
            model_name='starts',
            name='stars3',
            field=models.BigIntegerField(blank=True, default=0, verbose_name='三星评价'),
        ),
        migrations.AlterField(
            model_name='starts',
            name='stars4',
            field=models.BigIntegerField(blank=True, default=0, verbose_name='四星评价'),
        ),
        migrations.AlterField(
            model_name='starts',
            name='stars5',
            field=models.BigIntegerField(blank=True, default=0, verbose_name='五星评价'),
        ),
    ]
