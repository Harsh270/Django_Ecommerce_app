from django.db import models

class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50, default='')
    Company=models.CharField(max_length=50,default='')
    Subcategory=models.CharField(max_length=50,default='')
    long_desc=models.CharField(max_length=2000, default='')
    price=models.IntegerField()
    product_desc=models.CharField(max_length=300)
    published_date=models.DateField()
    image=models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    user_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    query=models.CharField(max_length=1000)

    def __str__(self):
        return self.name
