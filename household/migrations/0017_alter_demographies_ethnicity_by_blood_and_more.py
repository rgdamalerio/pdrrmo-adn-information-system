# Generated by Django 4.1 on 2022-09-27 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("household", "0016_alter_hhlivelihoods_area"),
    ]

    operations = [
        migrations.AlterField(
            model_name="demographies",
            name="ethnicity_by_blood",
            field=models.CharField(
                blank=True,
                max_length=150,
                null=True,
                verbose_name="Belongs to tribe/enthics",
            ),
        ),
        migrations.AlterField(
            model_name="demographies",
            name="extension",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name="demographies",
            name="nuclear_family",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="household.demographies",
                verbose_name="Nuclear family belongs to",
            ),
        ),
    ]
