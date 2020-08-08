from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import EventregisteruserForm,Eventregistertable,UserLoginForm, SecurityQuestionsForm,PasswordForm,ContactForm,PasswordVerificationForm       #RegisterProfileForm,ModuleMasterForm,AddServices,pharamcy,laboratorylab,labo ,labo1,
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import SecurityQuestions,Contact,Webregister               #,AddOnServices,pharamcytab,Labour,Emptytext,Empty,, ModuleMaster,
from django.http import Http404
from django.contrib import messages
from django.views.generic import ListView
from django.http import JsonResponse
import requests
import json
from django.core.exceptions import ValidationError
import phonenumbers
#from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import get_user_model
User = get_user_model()

# @csrf_exempt
# def partner_visibility(request):
# 	if request.method == 'POST':
# 		print(request.user,'request.user')
# 		form = EventregisteruserForm(request.POST)
# 		profileform = EventregisteruserForm(request.POST, request.FILES)
# 		print(form.is_valid)
# 		if form.is_valid() and profileform.is_valid():
# 			user = form.save()
# 			profile = profileform.save(commit=False)
#
# 			profile.user = user
#
# 			if 'header_eventimage' in request.FILES:
#
# 				profile.picture = request.FILES['header_eventimage']
# 				profile.save()
#
# 		else:
# 			return redirect('/partner_visibility',
# 							messages.success(request, 'form is invalid', 'alert-success'))
# 	else:
# 		form1 = EventregisteruserForm()
# 		form2 = EventregisteruserForm()
# 	return render(request, 'partner_visbility.html', {'form1': form1, 'form2': form2})

def partner_visibility(request):
	if request.method == 'POST':
		print(request.user,'request.user')
		form = EventregisteruserForm(request.POST, request.FILES)
		if form.is_valid():
			form = form.save(commit=False)
			if 'header_eventimage' in request.FILES:
				form.picture = request.FILES['header_eventimage']
				form.save()

		else:
			return redirect('/partner_visibility',
							messages.success(request, 'form is invalid', 'alert-success'))
	else:

		form = EventregisteruserForm()
	return render(request, 'partner_visbility.html', {'form':form})

@csrf_exempt
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		name = request.POST.get('name')
		print(form.errors)
		if form.is_valid():
			if form.save():
				return redirect('/contact', messages.success(request, 'Thank you for contacting Us. Our team will contact you as soon as earliest.', 'alert-success'))
			else:
				return redirect('/contact', messages.error(request, 'Something went wrong!', 'alert-danger'))
		else:
			return redirect('/contact', messages.error(request, 'Form is not valid', 'alert-danger'))
	else:
		form1 = ContactForm()
		return render(request, "Contact_Us.html", {'form':form})


@csrf_exempt
def contact_master(request):
	module = Contact.objects.all()
	return render(request, "Contact_Us_List.html", {'module': module})


@csrf_exempt
def password_reset(request):
	form = PasswordForm(request.POST or None)
	form1 = PasswordVerificationForm(request.POST or None)

	if request.method == 'POST':
		question = request.POST.get('question')
		answer = request.POST.get('answer')
		phone_no = request.POST.get('phone_no')
		print("question",question)
		print("answer",answer)
		print("phone_no",phone_no)
		check = SecurityQuestions.objects.get(id=1)   #change it when adding security question
		print(check.answer)
		if check.answer == answer:
			data_json = {"error" : False, "errorMessage" : "Correct Answer"}
			return JsonResponse(data_json, safe=False)
		else:
			data_json = {"error" : True, "errorMessage" : "Incorrect Answer"}
			return JsonResponse(data_json, safe=False)
	else:
		form = PasswordForm()
		form1 = PasswordVerificationForm()
	return render(request,"forget_password.html", {"form": form, "form1":form1})

@login_required
@csrf_exempt
def change_password(request):
	form = PasswordForm()
	if request.method == 'POST':
		print("dfdssgddddddddddddddddddddddddddddddddddddddddddddddddddddd")
		password = request.POST.get('password')
		password_confirm = request.POST.get('password_confirm')
		if password != password_confirm:
			print("mismatch")
			data_json = {"error" : True, "errorMessage" : "Password Mismatch"}
			return JsonResponse(data_json, safe=False)
		else:
			request.user.password = make_password(password)
			request.user.save()
			print("success")
			data_json = {"error" : False, "errorMessage" : "Password Changed"}
			return JsonResponse(data_json, safe=False)
	return render(request,"forget_password.html", {"form": form})

@login_required
@csrf_exempt
def send_otp(request):
	if request.method == "GET":
		#url = "https://api.msg91.com/api/v5/otp?authkey=95631AQvoigMsq5ec52866P1&template_id=5ec52d2dd6fc050944666272&mobile=+919702221660&invisible=1&otp=OTP to send and verify. If not sent, OTP will be generated.&userip=IPV4 User IP&email=Email ID"
		url = "https://api.msg91.com/api/v5/otp?authkey=95631AQvoigMsq5ec52866P1&template_id=5ec52d2dd6fc050944666272&mobile=+919702221660&invisible=1&userip=IPV4 User IP&email=Email ID"
		response = requests.request("GET",url)
		data = response.json()
		print("data",data)
		data_json = {"error" : False, "errorMessage" : "OTP Sent to your phone"}
	else:
		data_json = {"error" : True, "errorMessage" : "Failed to send OTP"}
	return JsonResponse(data_json)

@login_required
@csrf_exempt
def verify_otp(request):
	if request.method == "POST":
		otptxt = request.POST.get('phone_no')
		url = 'https://api.msg91.com/api/v5/otp/verify?mobile=+919702221660&otp='+str(otptxt)+'&authkey=95631AQvoigMsq5ec52866P1'
		print(url)
		response = requests.request("POST",url)
		data = response.json()
		print("data",data)
		data_json = {"error" : False, "errorMessage" : "OTP verified"}
	else:
		data_json = {"error" : True, "errorMessage" : "Fail to verify"}
	return JsonResponse(data_json)

@csrf_exempt
def login_view(request):
	next = request.GET.get("next")
	check = User.objects.get(id=1)
	print("last login",check.last_login)
	if check.last_login != None:
		form = UserLoginForm(request.POST or None)
		if form.is_valid():
			print("form valided")
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username = username, password = password)
			if not user:
				print("first")
				return redirect('/accounts/login/', messages.error(request, 'Username or password is incorrect', 'alert-danger'))
			login(request, user)
			print("login done")
			if next:
				return redirect(next)
			return redirect('eventtable')      #home
		return render(request, "login.html", {'form': form})
	else:
		form = UserLoginForm(request.POST or None)
		form1 = SecurityQuestionsForm(request.POST or None)
		#print("length of form",form1)
		if form.is_valid() and form1.is_valid():
			form1.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username = username, password = password)
			if not user:
				print("second")
				return redirect('/accounts/login/', messages.error(request, 'Username or password is incorrect', 'alert-danger'))
			login(request, user)
			if next:
				return redirect(next)
			return redirect('eventtable')           #home
		return render(request, "login.html", {'form': form, 'form1':form1})

def logout_view(request):
	logout(request)
	return redirect('/')

@csrf_exempt
def home(request):
	return render(request,"index.html", {})

@csrf_exempt
def eventregister(request):
	if request.method == 'POST':
		form = Eventregistertable(request.POST)
		print(form.errors)
		if form.is_valid():
			if form.save():
				return redirect('/eventtable',
								messages.success(request, 'Event is successfully updated.', 'alert-success'))
			else:
				return redirect('/eventtable', messages.error(request, 'Event is not saved', 'alert-danger'))
		else:
			return redirect('/eventtable', messages.error(request, 'Event is not valid', 'alert-danger'))
	else:
		form = Eventregistertable()
		return render(request,'event.html', {'form': form})

@csrf_exempt
def eventtable(request):
     module=Webregister.objects.all().values()
     return render(request,"eventtable.html",{'module':module})

def link(request,module_id):
    if request.method=='POST':
        module=Webregister.objects.get(id=module_id)
        id = form.cleaned_data.get('module_name')
        streaming_link = form.cleaned_data.get('module_code')

def registerlink(request, module_id):
    module = Webregister.objects.get(id=module_id)
    if request.POST:
        form = Eventregistertable(request.POST, instance=module)
        if form.is_valid():
            if form.save():
                return redirect('/eventregister', messages.success(request, 'Event is successfully updated.', 'alert-success'))
            else:
                return redirect('/eventregister', messages.error(request, 'Event is not saved', 'alert-danger'))
        else:
            return redirect('/eventregister', messages.error(request, 'Event is not valid', 'alert-danger'))
    else:
        form = Eventregistertable(instance=module)
        return render(request, 'editevent.html', {'form':form})

def editevent(request, module_id):
    module = Webregister.objects.get(id=module_id)
    if request.POST:
        form = Eventregistertable(request.POST, instance=module)
        if form.is_valid():
            if form.save():
                return redirect('/eventregister', messages.success(request, 'Event is successfully updated.', 'alert-success'))
            else:
                return redirect('/eventregister', messages.error(request, 'Event is not saved', 'alert-danger'))
        else:
            return redirect('/eventregister', messages.error(request, 'Event is not valid', 'alert-danger'))
    else:
        form = Eventregistertable(instance=module)
        return render(request, 'editevent.html', {'form':form})

def destroyevent(request, module_id):
    module = Webregister.objects.get(id=module_id)
    module.delete()
    return redirect('/eventtable', messages.success(request, 'Module is successfully deleted.', 'alert-success'))

# @csrf_exempt
# def partner_visibility(request):
#     if request.method == 'POST':
#         form = eventvisible(request.POST)
#         profileform = eventvisible(request.POST,request.FILES)
#         if form.is_valid() and profileform.is_valid():
#             user = form.save()
#             profile = profileform.save(commit=False)
#             profile.save()
#             profile.user = user
#
#         if 'header_eventimage' in request.FILES:
#
#             profile.picture = request.FILES['header_eventimage']
#             profile.save()
#
#             return redirect('/partner_visibility', messages.success(request, 'Profile Successfully Updated.', 'alert-success'))
#         else:
#             return redirect('/partner_visibility', messages.success(request, 'Profile sucessfully updated', 'alert-success'))
#     else:
#         form1 = eventvisible()
#         form2 = eventvisible()
#     return render(request,'partner_visbility.html', {'form1':form1, 'form2': form2})





# @csrf_exempt
# def partner_visibility(request):
#     if request.method == 'POST':
#         form = eventvisible(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/partner_visibility',messages.success(request, 'Form submitted Succesfully.', 'alert-success'))
#     else:
#         form = eventvisible()
#     return render(request, 'partner_visbility.html', {'form': form})









