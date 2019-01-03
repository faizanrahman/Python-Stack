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
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UsersManager()

# Class for Quotes Validation. Don't forget to include QuotesManager and objects = QuotesManager()
#     Class for Quotes


class QuotesManager(models.Manager):
    def quote_validator(self, postData):
        errors = {}
        if len(postData['author']) < 3:
            errors["author"] = "Author has to be atleast 3 characters"
        if len(postData['user_quote']) < 10:
            errors['user_quote'] = 'Quote must be longer than 10 characters'
        
        return errors


class Quotes(models.Model):
    #author is the original person who said something.
    #logged in user is the one who just posted the quote.
    #user needs to be logged in to add quote 
    author= models.CharField(max_length=255)
    quote_text = models.TextField()
    uploader = models.ForeignKey(Users, related_name = 'quotes') 
    likes = models.ManyToManyField(Users, related_name = 'userlikes')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = QuotesManager()


    
    
    