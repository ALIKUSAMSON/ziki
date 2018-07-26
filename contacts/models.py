from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=100,help_text='50 characters max')
	email = models.EmailField(max_length=30)
	comment = models.TextField(default='messages sent')

	def __str__(self):
		return self.name