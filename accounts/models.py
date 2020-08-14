from django.db import models
from django.conf import settings

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import requests
import pytz
from django_countries.fields import CountryField
from django.core.validators import FileExtensionValidator

# def user_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return 'user_{0}/{1}'.format(instance.user, filename)

# def user_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return 'user_{0}/{1}'.format(instance.user, filename)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()



    def __str__(self):
        return self.email





class Webregister(models.Model):
    eventtitle = models.CharField(max_length=255)
    targetaudiance = models.CharField(max_length=255)
    eventtype = models.CharField(max_length=255)
    created_on = models.DateField(null=True,blank=True)
    end_on = models.DateField(null=True,blank=True)
    Chairpersons = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    mobilenumber = models.CharField(max_length=255)
    email = models.EmailField()
    Moderatorname = models.CharField(max_length=266)
    mmobile = models.CharField(max_length=255, blank=True)
    memail = models.EmailField()
    ContactPersonanme = models.CharField(max_length=255, blank=True)
    Cmobile = models.CharField(max_length=255)
    Cemail = models.EmailField()
    organizedby = models.CharField(max_length=255)
    sponserby = models.CharField(max_length=255, blank=True)
    Registerationrequired = models.CharField(max_length=266)
    # registerationrequired = models.CharField(choices=REGISTER_CHOICES, max_length=128)
    paymentrequired = models.CharField(max_length=255, blank=True)
    partnerrequired = models.CharField(max_length=255)
    creation_link = models.URLField(max_length=255,null=True,blank=True)
    register_link = models.CharField(max_length=255,null=True,blank=True)
    streaming_link = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.eventtitle

class Eventregisterationuser(models.Model):
    webregister = models.ForeignKey(Webregister,on_delete=models.CASCADE)
    header_eventimage = models.FileField(upload_to='images',null=True, blank=True)            #header_eventimage = models.ImageField(upload_to='images',null=True,blank=True,validators=[FileExtensionValidator(allowed_extensions=['jpeg'])])
    footer_eventimage = models.FileField(upload_to='images',null=True, blank=True)
    streaming_header = models.FileField(upload_to='images',null=True, blank=True)
    streaming_leftpanel = models.FileField(upload_to='images',null=True, blank=True)
    streaming_rightpanel = models.FileField(upload_to='images',null=True, blank=True)
    ticker_content = models.CharField(null=True, blank=True,max_length=255)
    ticker_time = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.pk)

class SecurityQuestions(models.Model):
    question = models.CharField(max_length=255, blank=True)
    answer = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.question


class Contact(models.Model):
    name = models.CharField(max_length=255, blank=True)
    phone_no = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    message = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name



# class RegisterProfile(models.Model):
#     user = models.OneToOneField('CustomUser', on_delete= models.CASCADE)
#     name = models.CharField(max_length=50)
#     email = models.EmailField()
#     password = models.CharField(max_length=50)
#     confirm_password = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.email






