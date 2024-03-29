# Generated by Django 4.2.10 on 2024-03-14 23:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_pdfdocument_product_location_product_methodology_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="pdfdocument",
            name="created",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="pdfdocument",
            name="filename",
            field=models.CharField(default="pdffile", max_length=64),
        ),
        migrations.AlterField(
            model_name="pdfdocument",
            name="name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="pdfdocument",
            name="pdf_file",
            field=models.FileField(blank=True, null=True, upload_to="pdf_files/"),
        ),
    ]
