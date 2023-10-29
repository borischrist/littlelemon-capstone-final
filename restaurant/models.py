from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from datetime import datetime

# Create your models here.

def validate_date(date):
    if date < datetime.now().date():
        raise ValidationError(str(date)+" is a date that has already passed")

class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.name
    

class MenuItem(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    inventory = models.PositiveSmallIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to="uploads/menuitem-img/", blank=True)
    
    def __str__(self):
        return str(self.id)+" - "+str(self.name)+" ("+str(self.category)+")"


class Booking(models.Model):
    client = models.ForeignKey(User,  on_delete=models.CASCADE, null=True)
    date = models.DateField(null=True)
    hour = models.SmallIntegerField(
        null=False,
        default=12,
        validators=[ #from 8am to 10pm
            MaxValueValidator(22),
            MinValueValidator(8)
        ],
    )
    
    class Meta:
        unique_together = ('date', 'hour')
                           
    def __str__(self):
        return str(self.id)+" - "+str(self.client)+" "+str(self.date)+" "+str(self.hour)+" hour"
    
    