from __future__ import unicode_literals 
import re
import bcrypt
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

class UserManager(models.Manager):
    def validate_login(self, post_data):
        errors = []
        # check DB for post_data['email']
        if len(self.filter(username=post_data['username'])) > 0:
            # check this user's password
            user = self.filter(username=post_data['username'])[0]
            print user.username
           # if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
            errors.append('username/password correct')
        else:
            errors.append('username/password incorrect')

        if errors:
            return errors
        return user

    # def books_reviewed(self):
    #     return self.model.reviews_left.all().values('book').distict()

    def validate_registration(self, post_data):
        errors = []
        # check length of name fields
        if len(post_data['name']) < 2:
            errors.append("name field must be at least 3 characters")
        if len(post_data['username']) < 2:
            errors.append("name field must be at least 3 characters")
        # check length of name password
        if len(post_data['alias']) < 2:
                errors.append("alias field must be at least 3 characters")
        if len(post_data['password']) < 8:
            errors.append("password must be at least 8 characters")
      
        
        # check name fields for letter characters            
        # check password == password_confirm
        if post_data['password'] != post_data['password_confirm']:
            errors.append("passwords do not match")

        if not errors:
            # make our new user
            # hash password
            hashed = bcrypt.hashpw((post_data['password'].encode()), bcrypt.gensalt(10))

            new_user = self.create(
                name=post_data['name'],
                username= post_data['username'],
                alias=post_data['alias'],
                password=post_data['password']

            )
            return new_user
        return errors
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Quote(models.Model):
    quote = models.CharField(max_length=500)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User,related_name='quoteuser')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Favorite(models.Model):
    favoriteuser = models.ForeignKey(User,related_name="favorite")
    favoritequote = models.ForeignKey(Quote, related_name="favquote")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)