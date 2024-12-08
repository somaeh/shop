from django.db import models



class Size(models.Model):
    title = models.CharField(max_length=10)
    
    
    def __str__(self):
        return self.title
    
class Color(models.Model):
    title = models.CharField(max_length=10)
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    discount = models.SmallIntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='prouducts')
    size = models.ManyToManyField(Size, related_name="products")
    color = models.ManyToManyField(Color, related_name="product")
    
    
    def __str__(self):
        return self.title
    
class Informations(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name="informations")
    text = models.TextField()
    
    def __str__(self):
        return self.text[:30]
