from django.db import models
from cloudinary.models import CloudinaryField

class Library(models.Model):
    title = models.CharField(max_length=100)
    description =models.TextField(blank=True, null= True)
    
    image = CloudinaryField('image')

