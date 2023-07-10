from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    #cascade means if user is deleted, just delete the profile but not the other way
    image = models.ImageField(default= 'default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    #__ is dunder method, tesle chai kunai object lai string ma represent garcha
    