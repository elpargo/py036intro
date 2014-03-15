from django.db import models

#Not recommended in real production code.
#because you mix presentation (choices in spanish)
#also because you need to recompile every time options change
RATING_CHOICES = (
    ('5', 'Sali un pro'),
    ('4', 'Lo entendi casi todo'),
    ('3', 'Entendi alguito'),
    ('2', 'Me perdi cuando hablo chino'),
    ('1', 'No entendi nada, lo solte en banda!'),
)

class Survey(models.Model):
	fullname = models.CharField(max_length=20)
 	email = models.EmailField(unique=True)
	rating = models.CharField(max_length=1,choices=RATING_CHOICES)
 	other_python_interests = models.CharField(max_length=500)
 	pyladies_interest = models.BooleanField()
 	coworking_interest = models.BooleanField()
 	satisfied_with_the_talk = models.BooleanField()
