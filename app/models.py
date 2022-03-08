from django.db import models

# Create your models here.
class UserReg(models.Model):
    name= models.CharField(max_length=50)
    email= models.CharField(max_length=100)
    password= models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)
    

