from django.db import models

class Survey(models.Model):
	fullname = models.CharField(20)
 	email = models.EmailField()
	rating = models.CharField(choices=[1,2,3,4,5])
 	other_python_interests = models.CharField(500)
 	pyladies_interest = models.BooleanField()
 	coworking_interest = models.BooleanField()
