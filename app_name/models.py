from django.db import models

# Create your models here.

class Class_Name(models.Model):
	field_1 = models.CharField(max_length=128,unique=True)
	field_2 = models.CharField(max_length=128,unique=True)

	# For Python 2
	def __unicode__(self):
		return self.field_1

	# For Python 3
	
	"""def __str__(self):
		return self.field_1"""
