from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="post",null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:  
        return f"user : {self.user.username}, post : {self.post}"

    
    
class Profile(models.Model):
    pic = models.ImageField(upload_to="pic",default="profile.png")
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str: 
        return self.user.username 




class CommentModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f"comment : {self.comment} user : {self.user}"





