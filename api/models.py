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