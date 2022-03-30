from socket import fromshare
from django.conf import settings
from django.utils import timezone
from django.db import models
from multiselectfield import MultiSelectField

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Robot(models.Model):

    name=models.CharField(max_length=100,default="name")
    faction=models.CharField(max_length=100,default=False)
    height=models.FloatField(default=1)
    weight=models.FloatField(default=1)
    weapon=models.IntegerField(default=1)

    def __str__(self):
        return "{}".format(self.name)


class Pilot(models.Model):
    pilih =(
    ("Male", "Male"),
    ("Female", "Female"),
)

    name=models.CharField(max_length=100,default='pilot name')
    age=models.IntegerField(default=20)
    experience=models.IntegerField(default=1)
    gender=MultiSelectField(choices=pilih,default="gender")
    robots=models.ForeignKey(Robot,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return "{}".format(self.name)
