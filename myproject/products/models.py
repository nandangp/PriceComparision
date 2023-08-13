from django.db import models


class product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    stock= models.IntegerField()
    image_url=models.CharField(max_length=2083)

class Contact(models.Model):
    name =models.CharField(max_length=120)
    email =models.CharField(max_length=120)
    message =models.CharField(max_length=122)

    def __str__(self):
        return self.name
    
    

   
    
    
