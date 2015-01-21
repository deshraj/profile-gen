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
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from progen.models import * 
from datetime import datetime,timedelta
import random,string
def home(request):
	# if request.user.is_authenticated():
	# 	return HttpResponseRedirect("/profile")
	# else:
	return render_to_response("index.html",context_instance=RequestContext(request))

def signup(request):
	if not request.user.is_active:
		if request.POST:
			print "entered the if sectison"
			username = request.POST['username']
			email = request.POST['email']
			password = request.POST['password']
			firstname = request.POST['firstname']
			lastname = request.POST['lastname']
			try:
				user = User.objects.create_user(username=username,email=email,password=password,first_name=firstname,last_name=lastname)
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

# donot delete this function as it may be used in future for the purpose of logout to a specific page
# def logout_view(request):
# 	logout(request)
# 	# return HttpResponseRedirect("/")
# 	return render_to_response("index.html",{'logout':1},context_instance=RequestContext(request))
def profile(request):
	userr = request.user.username	
	if request.user.is_authenticated() :
		try:
			UserDetails.objects.get(user= userr )
			new = 0
		except: 
			new = 1
		if new==1:
			newProfile(request)
		else:
			#write the queries for updating the user 
			updateProfile(request)
		return	render_to_response("create.html",{'user':request.user},context_instance=RequestContext(request))
	else:
		return redirect('/login/?next=%s' % request.path)

def stupro(request,username=None):
	#write the queries for getting the details of the user
	return render_to_response("display.html")

def create(request):
	if request.user.is_authenticated():
		return render_to_response("create.html",context_instance=RequestContext(request))
	else:
		return render_to_response("index.html",context_instance=RequestContext(request))

def newProfile(request):
	print "$$$$$$$$$$$$$$$$$$$$$$$$$$$ THE USER IS GOING TO CREATE THE PROFILE $$$$$$$$$$$$$$$$$$$$$$$$$$$$"
	if request.POST:
		print "CAUGHT THE POST REQUEST"
		username = request.user.username
		name = request.POST['name']
		email = request.POST['email']
		url = request.POST['url']
		phnum = request.POST['phnum']
		_10thScore = request.POST['10thScore']
		_10thFrom = request.POST['10thFrom']
		_12thScore = request.POST['12thScore']
		_12thFrom = request.POST['12thFrom']
		branch = request.POST['branch']
		semMarks = request.POST.getlist('semMarks')
		skillss = request.POST.getlist('skills')
		projectName = request.POST.getlist('projectName')
		projectDescription = request.POST.getlist('projectDescription')
		EOrI = request.POST.getlist('EOrI')
		intrests = request.POST.getlist('intrests')
		achievements = request.POST.getlist('achievements')

		print name
		print email
		print url
		print phnum
		print _10thScore
		print _12thScore
		print branch
		print semMarks
		print skillss
		print projectName
		print projectDescription
		print EOrI
		print intrests
		print achievements
		# _id = User.objects.filter(username=request.user.username)
		# education.objects.create(_10thPercent=_10thScore,_12thPercent=_12thScore,_10thSchool = _10thFrom,_12thSchool = _12thFrom, btech1stSem = semMarks[0], btech2ndSem = semMarks[1], btech3rdSem = semMarks[2], btech4thSem = semMarks[3], btech5thSem = semMarks[4], btech6thSem = semMarks[5], btech7thSem = semMarks[6], btech8thSem = semMarks[7]).save()
		UserDetails.objects.create(user = username,branch = branch, phno = phnum).save()
		Education.objects.create(user = username,_10thPercent=_10thScore,_12thPercent=str(_12thScore),_10thSchool = _10thFrom,_12thSchool = _12thFrom,btechmarks = semMarks).save()
		Skills.objects.create(user = username,skillsSet = skillss).save()
		Projects.objects.create(user = username,title = projectName, description = projectDescription).save()
		Experience.objects.create(user = username,expDesc = EOrI).save()
		Achievements.objects.create(user = username,desc = achievements).save()
		Intrests.objects.create(user = username,description = intrests).save()
		# print "the authenticated user is ", username

def updateProfile(request):
	print "######################## THE USER IS GOING TO UPDATE THE PROFILE ###########################"
	# WRITE THE QUERIES FOR UPDATING THE WHOLE USER DETAILS 
	return "hello"