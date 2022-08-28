from django.db import models

# Create your models here.

class info(models.Model):
 
    end_year=models.CharField(max_length=500,blank=True)
    intensity=models.CharField( max_length=500,blank=True)
    sector=models.CharField(max_length=200,blank=True)
    topic=models.CharField(max_length=500,blank=True)
    insight=models.CharField(max_length=500,blank=True)
    url=models.URLField(blank=True)
    region=models.CharField(max_length=500,blank=True)
    start_year=models.CharField(max_length=500,blank=True)
    impact=models.CharField(max_length=50,blank=True)
    added=models.CharField(max_length=500, blank=True)
    published=models.CharField(max_length=500,blank=True)
    country=models.CharField(max_length=500,blank=True)
    relevance=models.CharField(max_length=500,blank=True)
    pestle=models.CharField(max_length=500,blank=True)
    source=models.CharField(max_length=500,blank=True)
    title=models.CharField(max_length=500,blank=True)
    likelihood=models.CharField(max_length=500,blank=True)

# def __str__(self):
#     return self.id
    
     