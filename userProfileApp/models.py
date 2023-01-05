from django.db import models
from django.contrib.auth.models import AbstractUser 
from .managers import CustomeUserManager


    

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=50, unique=True, error_messages={"unique":"The email must be unique!"})
    profile_image = models.ImageField(null = True,blank = True,upload_to = "0_Profile-Picture")
    phone_number = models.CharField(max_length=250, null=True, blank=True)
    post_office = models.CharField(max_length=250, null=True, blank=True)
    thana = models.CharField(max_length=250, null=True, blank=True)
    district = models.CharField(max_length=250, null=True, blank=True)
    zipcode = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=264, null=True, blank=True)
    REQUIRES_FIELDS = ["email"]
    objects = CustomeUserManager()

    def __str__(self):
        return f"{self.pk}.{self.username}"    

    def get_profile_picture(self):
        url = ""
        try:
            url = self.profile_image.url
            
        except:
            url = ""
        return url
