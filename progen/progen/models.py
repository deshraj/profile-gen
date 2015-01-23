from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
	user = models.CharField(max_length = 70)
	branch = models.CharField(max_length = 500)
	phno  = models.CharField(max_length = 10)
	# url = models.CharField(max_length=1000)
class Education(models.Model):
	user = models.CharField(max_length = 70)
	t10thSchool = models.CharField(max_length =500)
	t10thPercent = models.CharField(max_length = 7)
	t12thSchool = models.CharField(max_length=500)
	t12thPercent = models.CharField(max_length=7)
	btechmarks = models.CharField(max_length = 100)

class Skills(models.Model):
	user = models.CharField(max_length = 70)
	skillsSet = models.CharField(max_length = 10000)

class Projects(models.Model):
	user = models.CharField(max_length = 70)
	title = models.CharField(max_length = 1000)
	description = models.CharField(max_length  = 30000)

class Experience(models.Model):
	user = models.CharField(max_length = 70)
	expDesc = models.CharField(max_length = 10000)

class Achievements(models.Model):
	user = models.CharField(max_length = 70)
	desc = models.CharField(max_length = 10000)

class Intrests(models.Model):
	user = models.CharField(max_length = 70)
	description = models.CharField(max_length = 10000)