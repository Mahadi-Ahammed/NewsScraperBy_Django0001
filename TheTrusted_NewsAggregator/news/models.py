from email.mime import image
from pickle import TRUE
from django.db import models
class Headline(models.Model):
    title = models.CharField(max_length=200,null=False)
    image = models.URLField(null=True,blank=True)
    url=models.TextField(unique=True)

    def __str__ (self):
        return self.title

# Create your models here.
