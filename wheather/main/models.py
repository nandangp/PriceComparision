from django.db import models

# Create your models here.
class Contact(models.Model):
    s_no =models.AutoField(primary_key=True)
    Name =models.CharField(max_length=255)
    Email=models.CharField(max_length=20)
    Content = models.TextField()

    def __str__(self):
        return self.Name
