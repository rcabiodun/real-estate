from django.db import models
import cloudinary
import cloudinary.uploader
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
from django.conf import settings


cloudinary.config(
    cloud_name="dtbezcndz",
    api_key="773231342284725",
    api_secret="AYoRvjgzRowXfqnLEiacnGiur9o"
)
# Create your models here.
PROPERTY_TYPES=(("HOUSE","HOUSE"),("FLAT","FLAT"))
class Appointment(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    day=models.CharField(max_length=20)
    price=models.CharField(max_length=20)
    email=models.EmailField()
    details=models.TextField(blank=True,null=True)

    def __str__(self) -> str:
        return self.firstname + self.lastname    

class Property(models.Model):
    
    caption=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    owner=models.CharField(max_length=20)
    price=models.IntegerField(default=0)
    bedroom=models.PositiveIntegerField(default=1)
    bathroom=models.PositiveIntegerField(default=1)
    landsize=models.IntegerField(default=1000)
    type=models.CharField(max_length=10,choices=PROPERTY_TYPES,null=True)
    buildingsize=models.IntegerField(default=1000)
    date_added=models.DateTimeField(auto_now_add=True)
    image_url=models.CharField(max_length=500,null=True,blank=True)
    image=models.ImageField(upload_to='imgs/property', blank=True)

    # @receiver(post_save,sender=Property)
    # def upload_property_image(sender,instance,**kwargs):
    #     if instance.image:
    #         cloudinary_response=cloudinary.uploader.upload(instance.image.path)
    #         instance.image_url=cloudinary_response["secure_url"]
    #         instance.save()

    def save(self,*args,**kwargs):
        if self.image:
            print(self.image.path)
            cloudinary_response=cloudinary.uploader.upload(self.image)
            self.image_url=cloudinary_response["secure_url"]
            
            super().save(*args,**kwargs)
            print("deleting copy")
            if cloudinary_response["secure_url"]:
                my_path=os.path.join(settings.BASE_DIR,'media')
                print(self.image)
                full_path=os.path.join(my_path1,self.image.name)
                print(full_path)
                os.remove(full_path)
