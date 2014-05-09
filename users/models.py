from django.db import models
from django.contrib.auth.forms import User

class User(models.Model):

  first_name = models.CharField('first name', max_length= 50)
  last_name = models.CharField('last name', max_length= 50)
  email = models.EmailField('email address')
  
  def __unicode__(self):
      return self.first_name
    