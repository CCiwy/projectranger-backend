# Generated by Django 5.0 on 2024-01-17 13:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("languages", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blueprint",
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
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="BlueprintLanguageWeight",
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
                ("weight", models.DecimalField(decimal_places=6, max_digits=6)),
                (
                    "blueprint",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blueprints.blueprint",
                    ),
                ),
                (
                    "language",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="languages.language",
                    ),
                ),
            ],
        ),
    ]
