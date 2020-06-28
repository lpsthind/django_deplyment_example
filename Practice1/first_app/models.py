from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=264)

    def __str__(self):
        return self.topic_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AcessRecords(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

    
#_______________________________________________________________________________________________   
#
#                           FOR LOGIN 
#_______________________________________________________________________________________________


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username