from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.forms import ModelForm
from .models import CustomUser,Webregister,Eventregisterationuser,SecurityQuestions,Contact  #RegisterProfile, ModuleMaster, ,AddOnServices,pharamcytab,Emptytext,Labour,Empty,Eventregister1
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
import os

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


class EventregisteruserForm(ModelForm):
    use_required_attribute = False
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(EventregisteruserForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['ticker_content'].required = False
        self.fields['ticker_time'].required = False

    header_eventimage = forms.ImageField(widget=forms.FileInput, required=False)        #,validators=[header_eventimage]
    footer_eventimage = forms.ImageField(widget=forms.FileInput, required=False)
    streaming_header = forms.ImageField(widget=forms.FileInput, required=False)
    streaming_rightpanel = forms.ImageField(widget=forms.FileInput, required=False)
    streaming_leftpanel = forms.ImageField(widget=forms.FileInput, required=False)
    # ticker_content = forms.CharField(widget=forms.TextInput(attrs={'required':'false'}))
    ticker_content = forms.CharField(required=False)
    ticker_time = forms.IntegerField(required=False)
    # ticker_time = forms.IntegerField(widget=forms.NumberInput(attrs={'required':'false'}))

    class Meta:
        model = Eventregisterationuser
        fields = ['header_eventimage','footer_eventimage','streaming_header','streaming_leftpanel','streaming_rightpanel','ticker_content','ticker_time']



    def clean_header_eventimage(self,*args,**kwargs):
        cleaned_data = super(EventregisteruserForm, self).clean()
        header_eventimage = cleaned_data.get("header_eventimage")
        check_file_extenstion = header_eventimage.name
        check = check_file_extenstion.split('.')[1]
        print(check, 'check')
        types = ['jpg', 'png', 'jpeg','PNG']
        if check not in types:
            raise forms.ValidationError("file format is wrong.")
        if header_eventimage:
            if header_eventimage.size > 1000 * 100:            #41937
                print("header_eventimage.size",header_eventimage.size)
                raise forms.ValidationError("File is too big.")

        return header_eventimage

    def clean_footer_eventimagee(self, *args, **kwargs):
        cleaned_data = super(EventregisteruserForm, self).clean()
        footer_eventimage = cleaned_data.get("footer_eventimage")
        check_file_extenstion = footer_eventimage.name
        check = check_file_extenstion.split('.')[1]
        print(check, 'check')
        types = ['jpg', 'png', 'jpeg', 'PNG']
        if check not in types:
            raise forms.ValidationError("file format is wrong.")
        if footer_eventimage:
            if footer_eventimage.size > 1000 * 100:
                print("reached froms.py")
                raise forms.ValidationError("File is too big.")

        return footer_eventimage

    def clean_streaming_header(self, *args, **kwargs):
        cleaned_data = super(EventregisteruserForm, self).clean()
        streaming_header = cleaned_data.get("streaming_header")
        # check_file_extenstion = streaming_header.name
        # check = check_file_extenstion.split('.')[1]
        # print(check, 'check')
        # types = ['jpg', 'png', 'jpeg', 'PNG']
        # if check not in types:
        #     raise forms.ValidationError("file format is wrong.")
        if streaming_header:
            if streaming_header.size > 1000 * 100:
                print("reached froms.py")
                raise forms.ValidationError("File is too big.")

        return streaming_header



    def clean_streaming_rightpanel(self, *args, **kwargs):
        cleaned_data = super(EventregisteruserForm, self).clean()
        streaming_rightpanel = cleaned_data.get("streaming_rightpanel")
        # check_file_extenstion = streaming_rightpanel.name
        # check = check_file_extenstion.split('.')[1]
        # print(check, 'check')
        # types = ['jpg', 'png', 'jpeg', 'PNG']
        # if check not in types:
        #     raise forms.ValidationError("file format is wrong.")
        if streaming_rightpanel:
            if streaming_rightpanel.size > 1000 * 100:
                print("reached froms.py")
                raise forms.ValidationError("File is too big.")

        return streaming_rightpanel

    def clean_streaming_leftpanel(self, *args, **kwargs):
        cleaned_data = super(EventregisteruserForm, self).clean()
        streaming_leftpanel = cleaned_data.get("streaming_leftpanel")
        # check_file_extenstion = streaming_leftpanel.name
        # check = check_file_extenstion.split('.')[1]
        # print(check, 'check')
        # types = ['jpg', 'png', 'jpeg', 'PNG']
        # if check not in types:
        #     raise forms.ValidationError("file format is wrong.")
        if streaming_leftpanel:
            if streaming_leftpanel.size > 1000 * 100:
                print("reached froms.py")
                raise forms.ValidationError("File is too big.")

        return streaming_leftpanel



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

# name = models.CharField(max_length=50)
#     email1 = models.CharField()
# #     password = models.CharField(max_length=50)
# class RegisterProfileForm(forms.ModelForm):
#
#
#     # name=
#     # email=
#     password = forms.CharField(widget=forms.PasswordInput())
#     confirm_password = forms.CharField(widget=forms.PasswordInput())
#     class Meta:
#         model = RegisterProfile
#         fields = ['name','email','password','confirm_password']
#
#     def clean(self):
#         cleaned_data = super(RegisterProfileForm, self).clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")
#
#         if password != confirm_password:
#             raise forms.ValidationError(
#                 "password and confirm_password does not match"
#             )


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
        model = Webregister
        fields = ['eventtitle', 'targetaudiance', 'eventtype', 'created_on', 'Chairpersons', 'name', 'mobilenumber',
                  'email', 'Moderatorname', 'mmobile', 'memail', 'ContactPersonanme', 'Cmobile', 'Cemail',
                  'organisedby', 'sponserby', 'Registerationrequired', 'paymentrequired', 'partnerrequired']


# class eventvisible(ModelForm):
    # user = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'date in days'}), required=False)
    # header_eventimage = forms.ImageField(widget=forms.FileInput, required=False)
    # footer_eventimage = forms.ImageField(widget=forms.FileInput, required=False)
    # streaming_header = forms.ImageField(widget=forms.FileInput, required=False)
    # streaming_rightpanel = forms.ImageField(widget=forms.FileInput, required=False)
    # streaming_leftpanel = forms.ImageField(widget=forms.FileInput, required=False)
    # active = forms.BooleanField(required=False)

    # class Meta:
    #     model = Eventregisterationuser
    #     fields = ['header_eventimage', 'footer_eventimage', 'streaming_header', 'streaming_rightpanel',
    #               'streaming_leftpanel', 'ticker_content', 'ticker_time']

