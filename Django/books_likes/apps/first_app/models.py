from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


class Books(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    uploader = models.ForeignKey(Users, related_name='books')
    likes = models.ManyToManyField(Users, related_name='user')
