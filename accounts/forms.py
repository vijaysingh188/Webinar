from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.forms import ModelForm
from .models import CustomUser,Eventregister1,Eventregisterationuser,SecurityQuestions,Contact  # ModuleMaster, ,AddOnServices,pharamcytab,Emptytext,Labour,Empty,Eventregister1
from django.core.validators import RegexValidator

from django_countries.fields import CountryField
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.contrib.auth.password_validation import validate_password
from django.core import validators
from accounts.validators import validate_password_digit, validate_password_uppercase,validate_pass
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from django.contrib.auth import get_user_model
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = CustomUser
		fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUser
		fields = ('email',)


class  EventregisteruserForm(ModelForm):
    class Meta:
        model = Eventregisterationuser
        fields = ['header_eventimage','footer_eventimage','streaming_header','streaming_leftpanel','streaming_rightpanel','ticker_content','frequency_ticket']



class UserLoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'User Name'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))


class SecurityQuestionsForm(ModelForm):
	question = forms.CharField(label='question', widget=forms.TextInput(attrs={'placeholder':'Security Question'}))
	answer = forms.CharField(label='answer', widget=forms.TextInput(attrs={'placeholder':'Answer'}))
	class Meta:
		model = SecurityQuestions
		fields = ['question','answer']

class PasswordForm(forms.Form):
	password = forms.CharField(disabled=True, widget=forms.PasswordInput(attrs={'placeholder':'New Password'}))
	password_confirm = forms.CharField(disabled=True, widget=forms.PasswordInput(attrs={'placeholder':'Re-enter Password'}))

class ContactForm(ModelForm):
	name = forms.CharField()
	phone_no = forms.CharField()
	email = forms.CharField()
	message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 5}))

	class Meta:
		model = Contact
		fields = ['name','phone_no','email','message']


class PasswordVerificationForm(forms.Form):
	question = forms.ModelChoiceField(disabled=True, queryset=SecurityQuestions.objects.all(), empty_label=None, widget=forms.Select(attrs={'class':'form-control','id': 'sectxt'}))
	answer = forms.CharField(disabled=True, label='answer', widget=forms.TextInput(attrs={'placeholder':'Answer','id': 'anstxt'}))
	phone_no = forms.CharField(disabled=True,label='phone_no', widget=forms.TextInput(attrs={'placeholder':'Enter OTP','id': 'otptxt'}))


class Eventregistertable(forms.ModelForm):
    eventtitle = forms.CharField(widget=forms.TextInput(attrs={}))
    doctor_options = (
        ('HDC', 'HDC'),
        ('Individual', 'Individual'),
        ('Both', 'Both')
    )
    targetaudiance = forms.ChoiceField(choices=doctor_options)
    doctor_options = (
        ('Webinar', 'webinar'),
        ('Conference', 'Conference'),
    )
    eventtype = forms.ChoiceField(choices=doctor_options)
    created_on = forms.DateField(widget=forms.DateInput(attrs={'id': 'datetime_from'}, format='%d/%m/%Y'),
                                 input_formats=settings.DATE_INPUT_FORMATS)
    Chairpersons = forms.CharField(required=False)
    name = forms.CharField(widget=forms.TextInput(), required=False)
    mobilenumber = forms.CharField(max_length=10, min_length=10, widget=forms.TextInput(), required=False)
    email = forms.EmailField(required=False)
    Moderatorname = forms.CharField(widget=forms.TextInput(), required=False)
    mmobile = forms.CharField(max_length=10, min_length=10, widget=forms.TextInput(), required=False)
    memail = forms.EmailField(required=False)
    ContactPersonanme = forms.CharField(widget=forms.TextInput(), required=False)
    Cmobile = forms.CharField(max_length=10, min_length=10, widget=forms.TextInput(), required=False)
    Cemail = forms.EmailField(required=False)
    organisedby = forms.CharField(widget=forms.TextInput(), required=False)
    sponserby = forms.CharField(widget=forms.TextInput(), required=False)
    CHOICES = (
        ('Yes', 'Yes'), ('No', 'NO'),
    )
    Registerationrequired = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)

    CHOICES = (
        ('Yes', 'Yes'), ('No', 'NO'),
    )
    paymentrequired = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)
    CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'NO'),
    )

    partnerrequired = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=False)

    class Meta:
        model = Eventregister1
        fields = ['eventtitle', 'targetaudiance', 'eventtype', 'created_on', 'Chairpersons', 'name', 'mobilenumber',
                  'email', 'Moderatorname', 'mmobile', 'memail', 'ContactPersonanme', 'Cmobile', 'Cemail',
                  'organisedby', 'sponserby', 'Registerationrequired', 'paymentrequired', 'partnerrequired']


# class ModuleMasterForm(ModelForm):
#    module_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Module Name'}))
#    module_code = CountryField()
#    no_of_patients =forms.CharField(max_length=233)
#    amount = forms.FloatField(widget=forms.TextInput(attrs={'id':'amount'}))
#    web_space=forms.CharField(widget=forms.PasswordInput(attrs={'id':'pwword'}),min_length=6, validators=[validate_password_digit, validate_password_uppercase,validate_pass])
#    cgst = forms.FloatField(widget=forms.TextInput(attrs={'id':'cgst'}))
#    sgst = forms.FloatField(widget=forms.TextInput(attrs={'id':'sgst'}))
#    gst = forms.FloatField(widget = forms.TextInput(attrs={'id':'gst','onfocus':'sum()'}))
#    total_amount = forms.FloatField(widget=forms.TextInput(attrs={'id':'tot_amount','onfocus':'sum1()'}))
#
#
#    def clean_email(self):
#       print(type(self.cleaned.data))
#       web_space=self.cleaned_data.get('web_space')
#       with open("ecommerce/disposible_email_provider.txt",'r') as f:
#          blacklist=f.read().splitlines()
#
#          for disposible_email in blacklist:
#             if disposible_email in web_space:
#                raise forms.validationError("gfhfhfgfgf" % disposible_email)
#
#    class Meta:
#       model = ModuleMaster
#       fields = ['module_name','module_code','no_of_patients','web_space','amount','cgst','sgst','gst','total_amount']



#
# class AddServices(ModelForm):
# 	add_onservices = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add_on service'}),required=False)
# 	add_on_servicescode = forms.IntegerField(widget=forms.TextInput(attrs={'id':'datepicker'}),required=False)
# 	amount =forms.IntegerField()
# 	cgst = forms.CharField(widget=forms.PasswordInput())
# 	sgst = forms.CharField(widget=forms.TextInput(attrs={'id':'email'}),required=False)
# 	gst  =forms.IntegerField()
#
#
#
#
#
#
# class pharamcy(ModelForm):
#    companyname=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'name'}))
#    addresslineone=forms.CharField(required=False)
#    addresslinetwo = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'address'}),required=False)
#    streetname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'streetname'}),required=False)
#    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'city'}),required=False)
#    country = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'country'}),required=False)
#    state = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'state'}),required=False)
#    pincode = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'pincode'}),required=False)
#    nationalhead = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'nationalhead'}))
#    contactnumber = forms.CharField(required=False)
#    emailaddress = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'email'}))
#    phonenumber = forms.CharField(widget=forms.PasswordInput(attrs={'id':'pwword'}),min_length=6, validators=[validate_password_digit, validate_password_uppercase,validate_pass])
#    regionalhead =forms.CharField(widget=forms.TextInput(attrs= {'placeholder':'head'}))
#    regionalcontactnumber = forms.CharField(required=False)
#    regionalemailaddress = forms.CharField(widget=forms.TextInput(attrs={'id':'datepicker'}))
#    regionalphonenumber = forms.CharField()
#    scientifichead = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'head'}),required=False)
#    scientificcontactnumber = forms.CharField(required=False)
#    scientificemailaddress = forms.EmailField(error_messages={'invalid': 'This is my email error msg.'}, widget=forms.TextInput(attrs={'class':'form-control', 'autocomplete':'off'}), required=False)
#    scientificphonenumber = forms.CharField(required=False)
#
#    def clean_email(self):
#       print(type(self.cleaned.data))
#       web_space=self.cleaned_data.get('web_space')
#       with open("ecommerce/disposible_email_provider.txt",'r') as f:
#          blacklist=f.read().splitlines()
#
#          for disposible_email in blacklist:
#             if disposible_email in web_space:
#                raise forms.validationError("gfhfhfgfgf" % disposible_email)
#
#    class Meta:
#        model = pharamcytab
#        fields = ['companyname','addresslineone','addresslinetwo','streetname','city','country','state','pincode','nationalhead','contactnumber','emailaddress','phonenumber','regionalhead','regionalcontactnumber','regionalemailaddress','regionalphonenumber','scientifichead','scientificcontactnumber','scientificemailaddress','scientificphonenumber']
#
#
# class laboratorylab(ModelForm):
#
#    investigationname=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'name'}),required=False)
#    synonyms=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Synonyms'}),required=False)
#    importantnotes=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'importantnotes'}),required=False)
#    GENDER_CHOICES=(
#     	('Yes-No','Yes-No'),
# 	    ('Present-Absent','Present-Absent'),
# 	    ('Seen-Not','Seen-Not Seen'),
# 	    ('Positive-Negative','Positive-Negative'),
# 	    ('Customize-Value','Customize-Value'),
#    )
#    selectdropdownlist=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect(),required=False)
#    select=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'select'}),required=False)
#    froms=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'date in days'}),required=False)
#    to = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'end date'}),required=False)
#    gender= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'gender'}),required=False)
#    umo1= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'umo1'}),required=False)
#    umo2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'umo2'}),required=False)
#    conversationfactor= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'factor'}),required=False)
#    GEEKS_CHOICES=(
#       ('high','True'),
#       ('low','False'),
#    )
#
#    refrencerange = forms.ChoiceField(choices=GEEKS_CHOICES,widget=forms.RadioSelect(),required=False)
#    GENDER_CHOICES=(
#       ('high','True'),
#       ('low','False'),
#    )
#    high = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect(),required=False)
#    class Meta:
#       model=Labour
#       fields=['id','investigationname','synonyms','importantnotes','selectdropdownlist','select','froms','to','gender','umo1','umo2','conversationfactor','refrencerange','high']
# class labo(ModelForm):
#    Labour=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'date in days'}),required=False)
#    froms=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'date in days'}),required=False)
#    to = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'end date'}),required=False)
#    gender= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'gender'}))
#    umo1= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'umo1'}),required=False)
#    umo2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'umo2'}),required=False)
#    conversationfactor= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'factor'}),required=False)
#    GEEKS_CHOICES=(
#       ('high','True'),
#       ('low','False'),
#    )
#
#    refrencerange = forms.ChoiceField(choices=GEEKS_CHOICES,widget=forms.RadioSelect(),required=False)
#    GENDER_CHOICES=(
#       ('high','True'),
#       ('low','False'),
#    )
#    high = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect(),required=False)
#
#
#    class Meta:
#       model=Emptytext
#       fields=['id','Labour','froms','to','gender','umo1','umo2','conversationfactor','refrencerange','high']
#
#
# class labo1(ModelForm):
#    Labour=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'date in days'}),required=False)
#    froms=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'date in days'}),required=False)
#    to = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'end date'}),required=False)
#    gender= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'gender'}),required=False)
#    umo1= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'umo1'}))
#    umo2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'umo2'}),required=False)
#    conversationfactor= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'factor'}),required=False)
#    GEEKS_CHOICES=(
#       ('high','True'),
#       ('low','False'),
#    )
#    refrencerange = forms.ChoiceField(choices=GEEKS_CHOICES,widget=forms.RadioSelect(),required=False)
#    GENDER_CHOICES=(
#       ('high','True'),
#
#       ('low','False'),
#    )
#    high = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect(),required=False)
#
#
#    class Meta:
#       model=Empty
#       fields=['id','Labour','froms','to','gender','umo1','umo2','conversationfactor','refrencerange','high']
#
