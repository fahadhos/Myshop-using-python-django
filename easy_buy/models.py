from django.db import models
import django.utils.datetime_safe
from django.utils import timezone


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=60)
    category = models.CharField(max_length=200, default="")
    subcategory = models.CharField(max_length=200, default="")
    mrp = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="easy_buy/images", default="")
    banner_image = models.ImageField(upload_to="easy_buy/banners", default="NULL")
    # is home mane home banner show on/oFF
    is_home = models.IntegerField(default=0)
    is_trandy = models.IntegerField(default=0)
    is_arrived = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    catstatus = models.IntegerField(default=0)
    desc = models.CharField(max_length=1000)
    brand = models.CharField(max_length=100, default="")
    discounted = models.CharField(max_length=10, default="")
    model = models.CharField(max_length=100, default="")
    pub_date = models.DateField("2022-05-16")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField
    name = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    subject = models.CharField(max_length=70, default="")
    message = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name
