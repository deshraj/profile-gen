from django.shortcuts import render
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.http import *
from django.conf import settings
from django.contrib import auth
# import mongoengine
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from datetime import datetime,timedelta
import random,string
# import settings
# import datetime
# from pyUrl.models import * 
# Create your views here.
def home(request):
	if user.is_authenticated:
		HttpResponseRedirect("/profile")
	else:
		return render_to_response("index.html",{'error':1},context_instance=RequestContext(request))

def signup(request):
	username = request.POST['username']
	email = request.POST['email']
	password = request.POST['password']
	user = User.objects.create_user(username=username,email=email,password=password)
	user.save()
	return HttpResponseRedirect("/profile")

def changepassword(request):
	if user.is_authenticated:
		if request.POST:
			username = user.username
			# email = request.POST['email']
			password = request.POST['password']
			user = User.objects.get(username=username)
			user.set_password(password)
			user.save()
	return HttpResponseRedirect("/profile")

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request,user)
        # Redirect to a success page.
        return HttpResponseRedirect("/profile")
    else:
        # Show an error page
        return HttpResponseRedirect("/logout")

def profile(request,username=None):
	if request.path=='/':
		return HttpResponseRedirect("/profile")
	else:

# def allotmentform(request):
# 	if request.POST:
# 		name = request.POST['name']
# 		univRoll = request.POST['univRoll']
# 		year = request.POST['year'],context_instance=RequestContext(request)
# 		mobile = request.POST['mobile']
# 		print name, univRoll, year, mobile
# 		# name = request.POST['name']
# 	return render_to_response('allotmentForm.html',context_instance=RequestContext(request))