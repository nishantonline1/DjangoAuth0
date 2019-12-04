from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from .utils import TimeStampable
from django.contrib.auth.models import User

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
Lowtax = 5
Medtax = 12
Avgtax = 18
Luxtax = 28

GST=((Lowtax,'5'),(Medtax,'12'),(Avgtax,'18'),(Luxtax,'28'))

class Supplier(TimeStampable, models.Model):
    supplierName = models.CharField(max_length=60)
    supplierCode = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.supplierName


class Product(TimeStampable, models.Model):
    productName = models.CharField(max_length=60)
    sku = models.CharField(max_length=10)
    salePrice = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    purchasePrice = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    gst = models.CharField(max_length=2, choices=GST, default=Avgtax)
    vendor = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.productName

class Address(TimeStampable, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='aduser')
    addressname=models.CharField(max_length=50)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    pincode=models.CharField(max_length=6)
    def __str__(self):
        return self.addressname

class Order(TimeStampable, models.Model):
    Offline = 'Offline'
    Online = 'Online'
    PaymentMethod = ((Offline, 'Offline'), (Online, 'Online'))
    OrderNo = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orduser')
    shipaddress = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='address')
    payment = models.CharField(max_length=10, choices=PaymentMethod, default=Offline)

    def __str__(self):
        return self.OrderNo


class OrderItem(TimeStampable, models.Model):
    Pending = 'Pending'
    Confirmed = 'Confirmed'
    Shipped = 'Shipped'
    Delivered = 'Delivered'
    OrderStatus = ((Pending, 'Pending'), (Confirmed, 'Confirmed'), (Shipped, 'Shipped'), (Delivered, 'Delivered'))
    orderid = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    productid = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    ordsale = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    ordpurchase = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    ordgst = models.CharField(max_length=2, choices=GST, default=Avgtax)
    orderitemstatus = models.CharField(max_length=15, choices=OrderStatus, default=Pending)
