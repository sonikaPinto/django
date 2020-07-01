from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)#username email password fname and lname
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)#sub directory under media

    def __str__(self):
        return self.user.username
