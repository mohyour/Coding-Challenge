# Generated by Django 3.0.3 on 2020-02-14 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excursions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excursion',
            name='duration',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='excursion',
            name='externalContent',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='excursion',
            name='featured',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='excursion',
            name='longDescription',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='excursion',
            name='mealInfo',
            field=models.CharField(blank=True, max_length=90),
        ),
        migrations.AlterField(
            model_name='excursion',
            name='minimumAge',
            field=models.CharField(blank=True, max_length=90),
        ),
        migrations.AlterField(
            model_name='excursion',
            name='shortDescription',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='excursion',
            name='wheelChairAccessible',
            field=models.BooleanField(),
        ),
    ]