from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=60)
    category = models.CharField(max_length=200, default="")
    subcategory = models.CharField(max_length=200, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="easy_buy/images", default="")
    desc = models.CharField(max_length=300)
    brand = models.CharField(max_length=100, default="")
    model = models.CharField(max_length=100, default="")
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name
