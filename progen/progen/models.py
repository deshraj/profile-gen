from django.db import models
from django.contrib.auth.models import User

# class userdetails(models.Model):
#     username = models.CharField(max_length = 8)
#     summary = models.CharField(max_length = 1000)
#     email = models.EmailField(max_length = 200)
#     skills = models.CharField(max_length=200)
#     def setfoo(self, x):
#         self.skills = json.dumps(x)

#     def getfoo(self, x):
#         return json.loads(self.skills)
# class Author(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=40)
#     email = models.EmailField()

class userDetails(models.Model):
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)

class education(models.Model):
	user = models.ForeignKey(User)
	_10thSchool = models.CharField(max_length =500)
	_10thPercent = models.CharField(max_length = 7)
	_12thSchool = models.CharField(max_length=500)
	_12thMarks = models.CharField(max_length=7)
	btech1stSem = models.CharField(max_length = 7)
	btech2ndSem = models.CharField(max_length = 7)
	btech3rdSem = models.CharField(max_length = 7)
	btech4thSem = models.CharField(max_length = 7)
	btech5thSem = models.CharField(max_length = 7)
	btech6thSem = models.CharField(max_length = 7)
	btech7thSem = models.CharField(max_length = 7)
	btech8thSem = models.CharField(max_length = 7)

class skills(models.Model):
	user = models.ForeignKey(User)
	skillsSet = models.CharField(max_length = 8)

class Projects(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length = 1000)
	description = models.CharField(max_length  = 3000)

class Experience(models.Model):
	user = models.ForeignKey(User)
	expDesc = models.CharField(max_length = 1000)

class Achievements(models.Model):
	uesr = models.ForeignKey(User)
	desc = models.CharField(max_length = 1000)