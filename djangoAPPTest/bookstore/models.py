from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=20,verbose_name='书名')
    price = models.DecimalField(max_digits=5,decimal_places=2,default=0.0)
    publish= models.CharField(max_length=20,verbose_name='图书出版社',default='清华出版社')