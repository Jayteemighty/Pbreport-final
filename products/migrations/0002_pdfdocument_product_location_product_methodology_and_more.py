# Generated by Django 4.2.10 on 2024-03-14 15:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PDFDocument",
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
                ("name", models.CharField(max_length=255)),
                ("pdf_file", models.FileField(upload_to="pdf_files/")),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="location",
            field=models.CharField(default="Your default location", max_length=255),
        ),
        migrations.AddField(
            model_name="product",
            name="methodology",
            field=models.CharField(
                default="Your default methodology", max_length=100000
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="objective",
            field=models.CharField(default="Your default objective", max_length=100000),
        ),
        migrations.AddField(
            model_name="product",
            name="report_code",
            field=models.CharField(
                default="Your default report code", max_length=100000
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="report_overview",
            field=models.CharField(
                default="Your default report overview", max_length=100000
            ),
        ),
    ]
