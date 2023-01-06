from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=3000)
    price = models.FloatField()
    category = models.CharField(max_length=200)
    image = models.ImageField(upload_to="products/")
    def __str__(self):
        return self.name

class User(models.Model):
    email = models.CharField(max_length=1000, primary_key=True)
    balance = models.FloatField(default=0.0)
    hash = models.CharField(max_length=64)
    def __str__(self):
        return self.email

class Favorite(models.Model):
    user = models.ForeignKey(User, to_field="email", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, to_field="id", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.email + " - " + self.product.name

    class Meta:
        unique_together = (('user', 'product'),)

class Location(models.Model):
    user = models.ForeignKey(User, to_field="email", on_delete=models.CASCADE)
    lat = models.FloatField(default=0.0)
    lng = models.FloatField(default=0.0)

    def __str__(self):
        return self.user.email + " - " + str(self.lat) + " - " + str(self.lng)
    
class Voucher(models.Model):
    code = models.CharField(max_length=1000, primary_key=True)
    discount = models.FloatField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.code