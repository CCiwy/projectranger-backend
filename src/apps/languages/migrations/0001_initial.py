# Generated by Django 5.0 on 2024-01-07 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('description', models.TextField(max_length=255)),
                ('paradigm', models.CharField(max_length=24)),
            ],
        ),
    ]
