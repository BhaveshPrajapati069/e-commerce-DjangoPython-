from pyexpat import model
from sre_constants import CATEGORY
from statistics import mode
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
STATE_CHOICES=(
    ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
    ('Andra Pradesh','Andra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Asam','Asam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Daman & Diu','Daman & Diu'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Harayan','Harayan'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('j & K','j & K'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Lakshadweep','Lakshdeep'),
    ('MP','MP'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Rajastan','Rajastan'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('West Bengal','West Bengal'),)


class Customer(models.Model):
 user=models.ForeignKey(User,on_delete=models.CASCADE)
 name=models.CharField(max_length=200)
 locality=models.CharField(max_length=200)
 city=models.CharField(max_length=50)
 zipcode=models.IntegerField()
 state=models.CharField(choices=STATE_CHOICES,max_length=50)

 def __str__(self):
    return str(self.id)

CATEGORY_CHOICES=(
  ('M','Mobile'),
  ('L','Laptop'),
  ('TW','Top Wear'),
  ('BW','Bottom Wear'),
)    
class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=100)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image=models.ImageField(upload_to='producting')

def __str__(self):
        return str(self.id)
    

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)

    def __str__(self):
     return str(self.id)

    @property
    def total_cost(self):
     return self.quantity * self.product.discounted_price   

STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way','On the way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)  
class OrderedPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')    

    @property
    def total_cost(self):
     return self.quantity * self.product.discounted_price   
