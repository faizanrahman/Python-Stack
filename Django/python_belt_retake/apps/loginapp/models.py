from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

# Create your models here.
class UsersManager(models.Manager):
    def basic_validator(self, postData):
        emailToCheck = postData['email']
        matchingEmail = Users.objects.filter(email=emailToCheck) 
        errors = {}
        if len(postData['first_name']) < 1:
            errors["first_name"] = "First Name cannot be blank"
        elif len(postData['first_name']) < 3:
            errors["first_name"] = 'First Name has to be atleast 3 characters'
        elif not re.match("^[A-Za-z]*$", postData['first_name']):
            errors["first_name"] = 'First Name can only contain letters. No numbers allowed!'


        if len(postData['last_name']) < 1:
            errors["last_name"] = "Last Name cannot be blank"
        elif len(postData['last_name']) < 3:
            errors["last_name"] = 'Last Name has to be atleast 3 characters'
        elif not re.match("^[A-Za-z]*$", postData['last_name']):
            errors["last_name"] = 'Last Name can only contain letters. No numbers allowed!'
        
        if len(postData['email']) < 1:
            errors['email'] = 'Email is required. Cannot be empty'
        elif len(matchingEmail) != 0:
            errors['email'] = 'Email already exists.'
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email'
        
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be atleast 8 characters'
        elif postData['password'] != postData['password_confirm']:
            errors["password"] = 'Must match password confirmation field'

        if len(postData['password_confirm']) < 1:
            errors['password_confirm'] = 'Password confirmation is required'


        

        return errors

    
    def login_validator(self, postData):
        emailToCheck = postData['email']
        matchingEmail = Users.objects.filter(email=emailToCheck)
        errors = {}

        if len(postData['email']) < 1:
            errors['email'] = 'Email is required. Cannot be empty'
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email'
        # elif len(matchingEmail) != 0:
        #     errors['email'] = 'Unknown email.'
        # else:
        #     emailToCheck = postData['email']
        #     matchingEmail = Users.objects.filter(email=emailToCheck)
        #     if len(MatchingEmail) == 0:
        #         errors['email'] = 'Unknown email'

        if len(postData['password']) < 1:
            errors['password'] = 'Password field cannot be blank'
        elif len(postData['password'])  < 8:
            errors['password'] = 'Password must be atleast 8 characters'

        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    # birthday = models.DateTimeField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UsersManager()

class WishManager(models.Manager):
    def wish_validator(self, postData):
        errors={}
        if len(postData['item']) < 1:
            errors['item'] = "Item is required"
        elif len(postData['item']) < 3:
            errors['item'] = "Item must be atleast 3 characters"
        
        if len(postData['desc']) < 1:
            errors['desc'] = 'Description is required'
        elif len(postData['desc']) < 3:
            errors['desc'] = "Description must be atleast 3 characters"

        return errors



class Wish(models.Model):
    item = models.CharField(max_length=255)
    description = models.TextField()
    granted = models.IntegerField(default=0) 
    uploader = models.ForeignKey(Users, related_name='wishes')
    likes = models.ManyToManyField(Users, related_name='user_likes')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = WishManager()