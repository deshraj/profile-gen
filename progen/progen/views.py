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
import random,string,ast
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
			u2 = userDetails.objects.get(user= userr )
			new = 0
		except: 
			new = 1
		if new==1:
			newProfile(request)
		else:
			#write the queries for updating the user 
			updateProfile(request)
		if new==1:
			return	render_to_response("create.html",{'user':request.user},context_instance=RequestContext(request))
		else:
			u2.btechmarks = [ item.encode('ascii') for item in ast.literal_eval(u2.btechmarks) ]
			u2.skillsSet = [ item.encode('ascii') for item in ast.literal_eval(u2.skillsSet)]
			u2.projectTitle = [ item.encode('ascii') for item in ast.literal_eval(u2.projectTitle)]
			u2.projectDesc = [ item.encode('ascii') for item in ast.literal_eval(u2.projectDesc) ]
			projects = zip(u2.projectTitle,u2.projectDesc)
			u2.expDesc = [ item.encode('ascii') for item in ast.literal_eval(u2.expDesc)]
			u2.achieveDesc = [ item.encode('ascii') for item in ast.literal_eval(u2.achieveDesc) ]
			u2.interestDesc = [ item.encode('ascii') for item in ast.literal_eval(u2.interestDesc) ]
			return render_to_response("create.html",{'user':request.user,'projects':projects,'u2':u2},context_instance=RequestContext(request))
	else:
		return redirect('/login/?next=%s' % request.path)

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

		a = userDetails.objects.create(user = username,branch = branch, phno = phnum, url = url,t10thPercent=_10thScore, t12thPercent=str(_12thScore),t10thSchool = _10thFrom,t12thSchool = _12thFrom,btechmarks = semMarks, skillsSet = skillss,projectTitle = projectName, projectDesc = projectDescription, expDesc = EOrI, interestDesc = intrests, achieveDesc = achievements)
		a.save()
		return	HttpResponseRedirect("/profile")

def updateProfile(request):
	print "######################## THE USER IS GOING TO UPDATE THE PROFILE ###########################"
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
		username = request.user.username
		userDetails.objects.filter(user = username ).update(branch = branch, phno = phnum, url = url,t10thPercent=_10thScore,t12thPercent=str(_12thScore),t10thSchool = _10thFrom,t12thSchool = _12thFrom,btechmarks = semMarks, skillsSet = skillss,projectTitle = projectName, projectDesc = projectDescription, expDesc = EOrI, achieveDesc = achievements, interestDesc = intrests)
		return HttpResponseRedirect("/profile")

def display(request,username=None):
	try:
		username = str(request.path[1:])
		u1 = User.objects.get(username = username)
		u2 = userDetails.objects.get(user = username )
		u2.btechmarks = [ item.encode('ascii') for item in ast.literal_eval(u2.btechmarks) ]
		u2.skillsSet = [ item.encode('ascii') for item in ast.literal_eval(u2.skillsSet)]
		u2.projectTitle = [ item.encode('ascii') for item in ast.literal_eval(u2.projectTitle)]
		u2.projectDesc = [ item.encode('ascii') for item in ast.literal_eval(u2.projectDesc) ]
		projects = zip(u2.projectTitle,u2.projectDesc)
		u2.expDesc = [ item.encode('ascii') for item in ast.literal_eval(u2.expDesc)]
		u2.achieveDesc = [ item.encode('ascii') for item in ast.literal_eval(u2.achieveDesc) ]
		u2.interestDesc = [ item.encode('ascii') for item in ast.literal_eval(u2.interestDesc) ]
		return render_to_response("display.html",{'u1':request.user,'u2':u2,'projects':projects},context_instance=RequestContext(request))
	except:
		return HttpResponse("<h3>The User has not signed up yet</h3>")