from django.contrib import admin
from .models import Product, Category, PDFDocument

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(PDFDocument)