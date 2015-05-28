from django.db import models

class Data(models.Model):
	roll = models.CharField(max_length=60)
	pwd = models.CharField(max_length=60)
	clg = models.CharField(max_length=60, default='PUSSGRC')
