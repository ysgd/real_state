from django.db import models

# Create your models here.
class Listing(models.Model):
  title = models.CharField(max_length=80)
  price = models.FloatField()
  num_beds = models.IntegerField()
  num_bathrooms = models.IntegerField()
  sq_ft = models.IntegerField()
  address = models.CharField(max_length=150)
  description = models.TextField()
  image = models.ImageField()
  
  def __str__(self):
    return self.title
  