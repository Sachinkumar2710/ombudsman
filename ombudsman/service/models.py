from django.db import models
class Service(models.Model):
    user_name=models.CharField(max_length=50)
    user_email=models.EmailField(max_length=100)
    user_desc=models.TextField(max_length=200)
# Create your models here.
