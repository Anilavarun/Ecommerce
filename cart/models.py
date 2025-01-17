from django.db import models
from product.models import *

# Create your models here.

class cartlist(models.Model):
    cart_id=models.CharField(max_length=9999,unique=True)
    date_added=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class cartitems(models.Model):
    pr=models.ForeignKey(product,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quan=models.IntegerField()
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def total(self):
        return self.pr.price*self.quan