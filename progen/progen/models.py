from django.db import models
from django.contrib.auth.models import User

class userDetails(models.Model):
	user = models.CharField(max_length = 70)
	branch = models.CharField(max_length = 500)
	phno  = models.CharField(max_length = 10)
	url = models.CharField(max_length=1000)
	t10thSchool = models.CharField(max_length =500)
	t10thPercent = models.CharField(max_length = 7)
	t12thSchool = models.CharField(max_length=500)
	t12thPercent = models.CharField(max_length=7)
	btechmarks = models.CharField(max_length = 100)
	skillsSet = models.CharField(max_length = 10000)
	projectTitle = models.CharField(max_length = 1000)
	projectDesc = models.CharField(max_length  = 10000)
	expDesc = models.CharField(max_length = 10000)
	achieveDesc = models.CharField(max_length = 10000)
	interestDesc = models.CharField(max_length = 10000)