from django.db import models

# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class PropertyType(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Vtype(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class purpose(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Property(models.Model):
    name = models.CharField(max_length=50)
    description=models.TextField()
    purpose=models.ForeignKey(purpose,on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    locality=models.CharField(max_length=50)
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    land_area = models.CharField(max_length=50)
    electricity_available=models.BooleanField(default=False)
    source_of_water = models.CharField(max_length=50,blank=True,null=True)
    built_year = models.CharField(max_length=50,blank=True,null=True)
    buildin_area = models.CharField(max_length=50,blank=True,null=True)
    bedrooms = models.IntegerField(blank=True,null=True)
    bathrooms = models.IntegerField(blank=True,null=True)
    postedOn = models.DateTimeField(auto_now_add=True)
    ownership = models.CharField(max_length=50,blank=True,null=True)
    price=models.IntegerField()
    furniture_available=models.BooleanField(default=False)
    contact_name=models.CharField(max_length=50)
    contact_phone=models.CharField(max_length=50)
    contact_email=models.EmailField(blank=True,null=True)
    main_image=models.ImageField(upload_to='images/')
    image_2=models.ImageField(upload_to='images/',blank=True,null=True)
    image_3=models.ImageField(upload_to='images/',blank=True,null=True)
    image_4=models.ImageField(upload_to='images/',blank=True,null=True)
    image_5=models.ImageField(upload_to='images/',blank=True,null=True)
    image_6=models.ImageField(upload_to='images/',blank=True,null=True)
    image_7=models.ImageField(upload_to='images/',blank=True,null=True)
    image_8=models.ImageField(upload_to='images/',blank=True,null=True)
    image_9=models.ImageField(upload_to='images/',blank=True,null=True)
    premium=models.BooleanField(default=False)
    def __str__(self):
        return self.name


class Vehichle(models.Model):
    name = models.CharField(max_length=50)
    description=models.TextField()
    vehichle_type=models.ForeignKey(Vtype,on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    locality=models.CharField(max_length=50)
    fuel=models.CharField(max_length=50)
    reg_year=models.IntegerField()
    kilometers=models.IntegerField(blank=True,null=True)
    gear_Type=models.CharField(max_length=20,blank=True,null=True)
    postedOn = models.DateTimeField(auto_now_add=True)
    ownership = models.CharField(max_length=50,blank=True,null=True)
    price=models.IntegerField()
    contact_name=models.CharField(max_length=50)
    contact_phone=models.CharField(max_length=50)
    contact_email=models.EmailField(blank=True,null=True)
    main_image=models.ImageField(upload_to='images/')
    image_2=models.ImageField(upload_to='images/',blank=True,null=True)
    image_3=models.ImageField(upload_to='images/',blank=True,null=True)
    image_4=models.ImageField(upload_to='images/',blank=True,null=True)
    image_5=models.ImageField(upload_to='images/',blank=True,null=True)
    
    def __str__(self):
        return self.name
