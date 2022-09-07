from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        
        email_ready_exist = User.objects.filter(email=email).exists()
        password_is_less_than_four = (len(password) < 4) 
        if email_ready_exist:
            messages.info(request,"Email already exist")
            return redirect('register')
        elif password_is_less_than_four:
            messages.info(request,"Password is less than 4 characters")
            return redirect('register.login.html')
        else:
            user = User.objects.create_user(first_name = first_name,last_name=last_name,username=last_name,email=email,password=password)
            user.save()
            print('user save')
            messages.success(request,"User created. Enter credentials to login")
            
        return redirect('register')
         
              
    
    return render(request,'register.html') 


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            print('wrong credentials')
    return render(request,"login.html")







def logout(request):
    auth.logout(request)
    print('user successfully logout')
    return redirect('register')





