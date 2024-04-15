from django.db import models

class Bruger(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    addressLine1 = models.CharField(max_length=255)
    addressLine2 = models.CharField(max_length=255)
    zipCode = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    companyName = models.CharField(max_length=255)
    vatNumber = models.CharField(max_length=20)
    orderComment = models.TextField()
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    termsAccepted = models.BooleanField()
    receiveMarketing = models.BooleanField()

class CartItem(models.Model):
    user = models.ForeignKey(Bruger, on_delete=models.CASCADE, related_name='cart_items')
    currency = models.CharField(max_length=3)
    product_id = models.CharField(max_length=255)
    image_url = models.URLField()
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    rebate_percent = models.DecimalField(max_digits=5, decimal_places=2)
    rebate_quantity = models.IntegerField()
    upsell_product_id = models.CharField(max_length=255, null=True, blank=True)
