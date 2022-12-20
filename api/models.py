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
    def __str__(self):
        return self.email

class Follow(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, to_field="email", related_name="user_f", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, to_field="id", related_name="product_f", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.email + " " + self.product.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'product'], name='unique_follow')
        ]

class Purchase(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, to_field="email", related_name="user_p", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, to_field="id", related_name="product_p", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return self.user.email + " " + self.product.name