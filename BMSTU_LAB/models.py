from django.db import models

# Create your models here.


class Product(models.Model):
    Name_pos = models.CharField(max_length=30)
    inform = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'product'