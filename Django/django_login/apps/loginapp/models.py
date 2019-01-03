from django.db import models
import re

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
        
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be atleast 8 characters'
        elif postData['password'] != postData['password_confirm']:
            errors["password"] = 'Must match password confirmation field'


        

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