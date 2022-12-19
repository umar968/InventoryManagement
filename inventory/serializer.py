from rest_framework import serializers
from .models import Supplier, Shop


class ShopSerializer(serializers.ModelSerializer):
    # supplier_name = serializers.SlugRelatedField(slug_field='supplier', queryset=Supplier.objects.all())

    class Meta:
        model = Shop
        fields = ['shop_name']


class SupplierSerializer(serializers.ModelSerializer):
    shops_details = ShopSerializer(many=True)

    class Meta:
        model = Supplier
        fields = ['supplier_name', 'supplier_address', 'shops_details']

    def create(self, validated_data):
        suppliers_data = validated_data.pop('shops_details')
        supplier = Supplier.objects.create(**validated_data)
        for supplier_data in suppliers_data:
            Shop.objects.create(supplier=supplier, **supplier_data)
        return supplier
