# Generated by Django 4.1 on 2022-08-11 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("household", "0011_hhlivelihoods"),
    ]

    operations = [
        migrations.AddField(
            model_name="hhlivelihoods",
            name="area",
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
