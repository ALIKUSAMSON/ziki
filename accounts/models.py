from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(User):
	fields = ['username','email','password','password confirmation']

	def __str__(self):
		return self.username
