# Generated by Django 4.1 on 2022-10-06 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aggregate", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="familiesandpopulation",
            name="num_of_family",
            field=models.IntegerField(default=0),
        ),
    ]
