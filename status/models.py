from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UpdateStatus(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    img = models.ImageField(blank=True,null=True,upload_to = "status")
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.user.username 
    
    
    




