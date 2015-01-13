from django.db import models

class userdetails(models.Model):
    # url = models.CharField(max_length=100000)
    # shortUrl = models.CharField(max_length=100)
    username = models.CharField(max_length = 8)
    summary = models.CharField(max_length = 1000)
    email = models.EmailField(max_length = 200)
    skills = models.ListField(max_length = 1000)
    projects = models.TextField(max_length = False)
# class Author(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=40)
#     email = models.EmailField()