from django.db import models


from datetime import datetime, timezone






class client(models.Model):
    
    
    name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    mobile_no = models.CharField(max_length=15, null=True, blank=True) 
    mail = models.CharField(max_length=50, null=True, blank=True)
    desigination = models.CharField(max_length=50, null=True, blank=True)
    photo = models.FileField(upload_to='media/uploads/', null = True, blank = True) 
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    instagram = models.URLField(max_length=300, null=True, blank=True)
    twitter = models.URLField(max_length=300, null=True, blank=True)
    linkdin = models.URLField(max_length=300, null=True, blank=True)
    facebook = models.URLField(max_length=300, null=True, blank=True)
    website1 = models.URLField(max_length=300, null=True, blank=True)
    address_link = models.URLField(max_length=300, null=True, blank=True)
    random_key = models.CharField(max_length=64, unique=True)
    