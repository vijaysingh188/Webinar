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


class CustomUser(AbstractUser):
	username = None
	email = models.EmailField(_('email address'), unique=True)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CustomUserManager()



	def __str__(self):
		return self.email







class Eventregisterationuser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    header_eventimage = models.ImageField(null=True,blank=True)
    footer_eventimage = models.ImageField(null=True, blank=True)
    streaming_header = models.ImageField(null=True, blank=True)
    streaming_leftpanel = models.ImageField(null=True, blank=True)
    streaming_rightpanel = models.ImageField(null=True, blank=True)
    ticker_content = models.TextField(null=True, blank=True)
    frequency_ticket = models.TimeField()
    count_ticket = models.IntegerField()
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.active




class Eventregister1(models.Model):
    eventtitle = models.CharField(max_length=255)
    targetaudiance = models.CharField(max_length=255)
    eventtype = models.CharField(max_length=255)
    created_on = models.DateField()
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
    paymentrequired = models.CharField(max_length=255, blank=True)
    partnerrequired = models.CharField(max_length=255)

    def __str__(self):
        return self.eventtitle





class SecurityQuestions(models.Model):
	question = models.CharField(max_length=255, blank=True)
	answer = models.CharField(max_length=255, blank=True)

	def __str__(self):
	    return self.question

# class ModuleMaster(models.Model):
#   updated_on = models.DateTimeField(auto_now=True)
#   created_on = models.DateTimeField(auto_now_add=True)
#   module_name = models.CharField(max_length=255, blank=True)
#   module_code = CountryField(default="IN")
#   no_of_patients = models.IntegerField(default = 0)
#   web_space = models.CharField(max_length=255)
#   amount = models.FloatField(default = 0,blank=True)
#   cgst = models.FloatField(default = 0)
#   sgst = models.FloatField(max_length=11,blank=True)
#   gst = models.FloatField()
#   total_amount = models.FloatField(default = 0)
#
#
#   def __str__(self):
#     return self.module_name

class Contact(models.Model):
	name = models.CharField(max_length=255, blank=True)
	phone_no = models.CharField(max_length=255, blank=True)
	email = models.EmailField(max_length=255, blank=True)
	message = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.name

# class AddOnServices(models.Model):
#   updated_on = models.DateTimeField(auto_now=True)
#   created_on = models.DateTimeField(auto_now_add=True)
#   add_onservices = models.CharField(max_length=255)
#   add_on_servicescode = models.CharField(max_length=255)
#   amount = models.CharField(max_length=255)
#   cgst = models.FloatField(default = 0)
#   sgst = models.FloatField(default = 0)
#   gst = models.CharField(max_length=255)
#   def __str__(self):
#     return self.add_onservices


# class pharamcytab(models.Model):
#     companyname = models.CharField(max_length=255)
#     addresslineone=models.CharField(max_length=255)
#     addresslinetwo = models.CharField(max_length=255)
#     streetname = models.CharField(max_length=255)
#     city= models.CharField(max_length=255)
#     country= models.CharField(max_length=266)
#     state= models.CharField(max_length=255)
#     pincode= models.IntegerField(default = 0)
#     nationalhead= models.CharField(max_length=266)
#     contactnumber= models.CharField(max_length=255, blank=True)
#     emailaddress= models.EmailField()
#     phonenumber= models.CharField(max_length=255, blank=True)
#     regionalhead= models.CharField(max_length=255)
#     regionalcontactnumber= models.CharField(max_length=255, blank=True)
#     regionalemailaddress= models.CharField(max_length=255)
#     regionalphonenumber= models.CharField(max_length=255, blank=True)
#     scientifichead=models.CharField(max_length=266)
#     scientificcontactnumber= models.CharField(max_length=255, blank=True)
#     scientificemailaddress= models.EmailField()
#     scientificphonenumber=models.CharField(max_length=255, blank=True)
#     updated_on = models.DateTimeField(auto_now=True)
#     created_on = models.DateTimeField(auto_now_add=True)
#
#
#
#
#
#     def __str__(self):
#         return self.city
#
#
#
#
#
#
#
#
# class Emptytext(models.Model):
#    Labour=models.ForeignKey('Labour',on_delete=models.CASCADE,related_name='Emptytext')
#    froms= models.IntegerField()
#    to = models.IntegerField()
#    gender= models.CharField(max_length=255,blank=True)
#    umo1= models.CharField(max_length=255,blank=True)
#    umo2 = models.CharField(max_length=255,blank=True)
#    conversationfactor= models.CharField(max_length=255)
#    GENDER_CHOICES=(
#       ('high','high'),
#       ('low','low'),
#     )
#    refrencerange = models.CharField(choices=GENDER_CHOICES,max_length=10,verbose_name=umo1)
#    GENDER_CHOICES=(
#       ('high','high'),
#       ('low','low'),
#     )
#
#    high=models.CharField(choices=GENDER_CHOICES,max_length=10)
#
#
#
#    def __unicode__(self):
#     return u'%s' % (self.gender)
#
#     class Meta:
#       verbose_name=('gender')
#       verbose_name_plural=("gender")
#
#
#
#
# class Labour(models.Model):
#
#    investigationname=models.CharField(max_length=255)
#    synonyms = models.CharField(max_length=255)
#    importantnotes = models.CharField(max_length=255)
#    GENDER_CHOICES=(
#       ('Yes-No','Yes-No'),
#       ('Present-Absent','Present-Absent'),
#       ('Seen-Not','Seen-Not Seen'),
#       ('Positive-Negative','Positive-Negative'),
#       ('Customize-Value','Customize-Value'),
#    )
#
#    selectdropdownlist=models.CharField(choices=GENDER_CHOICES,max_length=20)
#    select=models.CharField(max_length=255)
#
#
#
#    def __unicode__(self):
#         return self.investigationname
#
#
# class Empty(models.Model):
#    laboratory_id=models.ForeignKey('Labour',on_delete=models.CASCADE)
#    froms= models.IntegerField()
#    to = models.IntegerField()
#    gender= models.CharField(max_length=255)
#    umo1= models.CharField(max_length=255)
#    umo2 = models.CharField(max_length=255)
#    conversationfactor= models.CharField(max_length=255)
#
#    refrencerange=models.CharField(max_length=255)
#    high=models.CharField(max_length=244)
#
#    def __str__(self):
#     return self.gender









