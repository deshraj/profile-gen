from django.shortcuts import render
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.http import *
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
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
	if request.user.is_authenticated():
		return HttpResponseRedirect("/profile")
	else:
		return render_to_response("index.html",context_instance=RequestContext(request))

def signup(request):
	if not request.user.is_active:
		if request.POST:
			print "entered the if sectison"
			username = request.POST['username']
			email = request.POST['email']
			password = request.POST['password']
			try:
				user = User.objects.create_user(username=username,email=email,password=password)
				user.save()
				return HttpResponseRedirect("/profile")
			except:
				return HttpResponse("This Id already exists")
		else:
			print "entered the else section"
			return render_to_response("register.html",context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/")	

def login(request):
	if not request.user.is_authenticated():
		if request.POST:
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
				return HttpResponse("<h3>Incorrect password</h3>")
		return render_to_response('login.html',context_instance=RequestContext(request))
	else:
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


# def logout_view(request):
# 	logout(request)
# 	# return HttpResponseRedirect("/")
# 	return render_to_response("index.html",{'logout':1},context_instance=RequestContext(request))
def profile(request):
	if request.user.is_authenticated() :
		print "the authenticated user is ", request.user.username
		return	render_to_response("profile.html",{'user':request.user},context_instance=RequestContext(request))
	else:
		return redirect('/login/?next=%s' % request.path)

def stupro(request,username=None):
	#write the queries for getting the details of the user
	return render_to_response("display.html")


# def allotmentform(request):
# 	if request.POST:
# 		name = request.POST['name']
# 		univRoll = request.POST['univRoll']
# 		year = request.POST['year'],context_instance=RequestContext(request)
# 		mobile = request.POST['mobile']
# 		print name, univRoll, year, mobile
# 		# name = request.POST['name']
# 	return render_to_response('allotmentForm.html',context_instance=RequestContext(request))