# Generated by Django 4.1 on 2022-08-09 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0015_evacuationareas"),
    ]

    operations = [
        migrations.AlterField(
            model_name="buildingroofmaterials",
            name="description",
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name="buildingstatus",
            name="status",
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name="buildingtypes",
            name="type",
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name="buildinguses",
            name="use",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="buildingwallmaterials",
            name="material",
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name="disabilities",
            name="description",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="evacuationareas",
            name="evacuation_area",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="farmingtechs",
            name="technology",
            field=models.CharField(max_length=125, unique=True),
        ),
        migrations.AlterField(
            model_name="genders",
            name="gender",
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="gradelevels",
            name="code",
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name="gradelevels",
            name="description",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="municipalities",
            name="munname",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
