# Generated by Django 4.2.2 on 2023-06-30 13:38

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('search_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='continent',
            name='mpoly',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(default=django.utils.timezone.now, srid=4326),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='mpoly',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(default=django.utils.timezone.now, srid=4326),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=django.utils.timezone.now, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=django.utils.timezone.now, max_digits=9),
            preserve_default=False,
        ),
    ]
