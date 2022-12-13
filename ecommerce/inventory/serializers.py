from rest_framework import serializers
from ecommerce.inventory.models import Category, Media, Product, Stock

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
        
       
class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
        ]
        
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
        ]
        
class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'sku',
            'upc',
            'product',
            'product_type',
            'brand',
            'is_active',
            'retail_price',
            'store_price',
            'sale_price',
            'sale_on_sale',
            'is_digital',
            'weight',
            'created_at',
            'updated_at',
        ]
        
class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
        ]
        
class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = [
            'product_inventory',
            'img_url',
            'alt_text',
            'is_feature',
            'created',
            'updated',
            
        ]
        
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = [
            'product_inventory',
            'last_checked'
            'units',
            'units_sold',
            
        ]
        
class ProductAttributeValues(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValues
        fields = [
            'name',
        ]