from django.db import models

# Create your models here.
class Contact(models.Model):
    s_no =models.AutoField(primary_key=True)
    Name =models.CharField(max_length=255)
    Email=models.CharField(max_length=20)
    Content = models.TextField()

    def __str__(self):
        return self.Name
    
class Prizes(models.Model):
    p_no = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=50)
    p_img = models.URLField()
    f_prize = models.CharField(max_length=50)
    a_prize = models.CharField(max_length=50)
    r_prize = models.CharField(max_length=50)

    def __str__(self):
        return self.p_name
