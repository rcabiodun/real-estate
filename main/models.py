from django.db import models

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
    image=models.ImageField(upload_to='imgs/property', blank=True)