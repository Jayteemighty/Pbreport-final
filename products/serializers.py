from rest_framework import serializers

from .models import  Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'category',
            'title',
            'slug',
            'description',
            'price',
            'date_added',
            'location',
            'report_code',
            'report_overview',
            'objective',
            'methodology',
            "get_absolute_url",
            "get_image",
            "get_thumbnail",
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "get_absolute_url",
            "products",
        )