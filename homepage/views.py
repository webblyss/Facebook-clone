from django.shortcuts import render
from .models import Post,CommentModel,Profile
from django.contrib import auth
from django.http import HttpResponseRedirect
from status.models import UpdateStatus

# Create your views here.


def homepage(request):
    post = Post.objects.all()
    user = auth.get_user(request)
    comments = CommentModel.objects.all()
    profile = Profile.objects.all()
    if request.method == 'POST':
        title = request.POST['post']
        img = request.FILES['img']
        post = Post.objects.create(post=title,image = img,user =user)
        post.save()
        print("post added successfully")
        
        return HttpResponseRedirect(request.path_info)
        
    
    return render(request,'homepage.html',{'post':post,"comments":comments,"profile":profile})

    






