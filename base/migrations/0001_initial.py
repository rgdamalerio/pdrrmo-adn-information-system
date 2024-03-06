# Generated by Django 4.1 on 2023-10-25 02:52

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdnFlood',
            fields=[
                ('gid', models.IntegerField(primary_key=True, serialize=False)),
                ('objectid', models.FloatField()),
                ('susc_ratin', models.CharField(max_length=255)),
                ('shape_leng', models.IntegerField()),
                ('shape_area', models.IntegerField()),
                ('descriptio', models.CharField(max_length=255)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
    ]