# Generated by Django 5.0.3 on 2024-03-22 22:59

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="createParcelRide",
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
                ("username", models.CharField(max_length=150)),
                ("source", models.TextField()),
                ("destination", models.TextField()),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Location",
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
                ("name", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Parcel",
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
                ("sender", models.CharField(max_length=150)),
                ("recipient", models.CharField(max_length=150)),
                ("source", models.TextField()),
                ("destination", models.TextField()),
                ("description", models.TextField()),
                ("weight", models.DecimalField(decimal_places=2, max_digits=5)),
                ("is_delivered", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="ParcelService",
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
                ("source", models.CharField(max_length=100)),
                ("destination", models.CharField(max_length=100)),
                ("description", models.TextField()),
            ],
        ),
    ]