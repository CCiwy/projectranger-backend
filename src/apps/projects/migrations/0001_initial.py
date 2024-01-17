# Generated by Django 5.0 on 2024-01-17 12:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("is_done", models.BooleanField(default=False)),
                ("is_public", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("github_url", models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="ProjectEntity",
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
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="ProjectIdea",
            fields=[
                (
                    "projectentity_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="projects.projectentity",
                    ),
                ),
            ],
            bases=("projects.projectentity",),
        ),
        migrations.CreateModel(
            name="ProjectNotes",
            fields=[
                (
                    "projectentity_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="projects.projectentity",
                    ),
                ),
            ],
            bases=("projects.projectentity",),
        ),
        migrations.CreateModel(
            name="ProjectTodos",
            fields=[
                (
                    "projectentity_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="projects.projectentity",
                    ),
                ),
            ],
            bases=("projects.projectentity",),
        ),
    ]
