from random import betavariate
from django.db import models

# Create your models here.

class WebBeta1(models.Model):
    service_name = models.CharField(max_length=200)
    ip1 = models.CharField(max_length=200,blank=True)
    ip2 = models.CharField(max_length=200,blank=True)
    ip3 = models.CharField(max_length=200,blank=True)
    ip4 = models.CharField(max_length=200,blank=True)
    ip5 = models.CharField(max_length=200,blank=True)
    
    def __str__(self):
        return self.service_name
        
class WebBeta2(models.Model):
    service_name = models.CharField(max_length=200)
    ip1 = models.CharField(max_length=200,blank=True)
    ip2 = models.CharField(max_length=200,blank=True)
    ip3 = models.CharField(max_length=200,blank=True)
    ip4 = models.CharField(max_length=200,blank=True)
    ip5 = models.CharField(max_length=200,blank=True)
    
    def __str__(self):
        return self.service_name    
    
class WebBeta3(models.Model):
    service_name = models.CharField(max_length=200)
    ip1 = models.CharField(max_length=200,blank=True)
    ip2 = models.CharField(max_length=200,blank=True)
    ip3 = models.CharField(max_length=200,blank=True)
    ip4 = models.CharField(max_length=200,blank=True)
    ip5 = models.CharField(max_length=200,blank=True)
    
    def __str__(self):
        return self.service_name
    
class WebBeta4(models.Model):
    service_name = models.CharField(max_length=200)
    ip1 = models.CharField(max_length=200,blank=True)
    ip2 = models.CharField(max_length=200,blank=True)
    ip3 = models.CharField(max_length=200,blank=True)
    ip4 = models.CharField(max_length=200,blank=True)
    ip5 = models.CharField(max_length=200,blank=True)
    
    def __str__(self):
        return self.service_name

class NewUpdateInfo(models.Model):
    name = models.CharField(max_length=100)
    beta = models.CharField(max_length=100)
    production = models.CharField(max_length=100)   

    def __str__(self):
        return self.name 

class RRFImage(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='pics')
    

class IPTable(models.Model):
    service_name = models.CharField(max_length=200)
    ip1 = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.ip1