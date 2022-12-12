from rest_framework import serializers
from ecommerce.inventory.models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'slug',
            'is_active',
            'parent',
        ]
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'web_id',
            'slug',
            'description',
            'is_active',
            'category',
            'created_at',
            'updated_at'
        ]