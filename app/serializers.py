from django.contrib.auth.models import User, Group
from rest_framework import serializers
from app.models import Product,Supplier,Order, Address


class UserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(required=True)
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('url','productName', 'sku', 'salePrice', 'purchasePrice','vendor', 'modified_at', 'created_at')

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ( 'supplierName', 'supplierCode', 'address', 'email', 'modified_at', 'created_at')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields = ('OrderNo','shipaddress','user','payment')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('addressname','city','state','pincode')