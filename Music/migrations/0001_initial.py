# Generated by Django 4.1 on 2023-04-27 03:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Music",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("music_name", models.CharField(max_length=50)),
                ("music_brand", models.CharField(max_length=100)),
                ("music_price", models.IntegerField(default=0)),
                ("music_buy", models.DateTimeField(default=django.utils.timezone.now)),
                ("music_producer", models.CharField(max_length=50)),
                ("music_quantity", models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
