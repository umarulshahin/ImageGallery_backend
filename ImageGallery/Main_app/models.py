from django.db import models
from django.utils import timezone
from Authentication_app.models import *
# Create your models here.

class Images(models.Model):
    
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/')
    descriptions = models.TextField(blank=False,null=False)
    created_at = models.DateTimeField(default=timezone.now)