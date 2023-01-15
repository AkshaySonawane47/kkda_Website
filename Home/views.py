from email import message
from django.shortcuts import render, HttpResponse , redirect
from datetime import datetime
from Home.models import Contact,admission_registration
from Home.models import  Post,Category
from django.contrib import messages
from Home.models import admission_registration 
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



# Create your views here.

   
def home(request):  

    if request.method == "POST":
        name = request.POST.get('name')
        email= request.POST.get('email')
        message=request.POST.get('message')
        home = Contact(name=name, email=email, message=message, date = datetime.today())
        home.save()
        messages.success(request, "Your Contact Message has been Sent ! Thank You " +name )
        # messages.success(request, 'Your Contact Message has been Sent!')
    
    
    post=Post.objects.all()
    cat=Category.objects.all()
    data={  'post': post ,
            'cat': cat 
       } 
    return render(request, 'index.html',data)


def about(request):
    # message.success(request, "this is succesfull done.")
    return render(request,'about.html')


@login_required(login_url='login') 
def base(request):
    # message.success(request, "this is succesfull done.")

    post=Post.objects.all()
    data={  'post': post    }
    
    return render(request,'base.html',data)

    # message.success(request, "this is succesfull done.")

# def posts(request,id):
#     pots = Post.objects.get(post_id=id)
#     posts = Post.objects.filter(url=pots)
#     context = { 'pots': pots, 'posts': posts}
#     return render(request,'posts.html', context)    

    # print(pots)
def posts(request):
    # message.success(request, "this is succesfull done.")

    post=Post.objects.all()
    data={  'post': post    }
    
    return render(request,'base.html',data)

def demo(request):
    # message.success(request, "this is succesfull done.")
    return render(request,'demo.html') 


# def base(request):
#     # message.success(request, "this is succesfull done.")

#     post=Post.objects.all()
#     data={  'post': post    }
    
#     return render(request,'base.html',data)


def submit_form(request):

    if request.method == "POST":
        firstname = request.POST.get('firstname')
        middlename = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        gender = request.POST.get('gender') 
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        email = request.POST.get('email')
        if  User.objects.filter(email=email).exists():
            messages.warning(request, "password and  user email wrong please type new email and password! ")
            return redirect('demo.html')
        else:
            print(firstname,middlename,lastname,gender,phone,address,email)
            msg = "Registration Successfully Done ! Thank You " 
            submit_form=admission_registration(firstname=firstname,middlename=middlename,lastname=lastname,gender=gender,phone=phone,address=address,email=email, date = datetime.today())
            submit_form.save()
            return render(request,'demo.html',{'msg': msg})
    else:
        return HttpResponse("404 - not found")

    
def register(request):
    
    if request.method == 'POST':
        uname =request.POST.get('username')
        email =request.POST.get('email')
        pass1= request.POST.get('password1')
        pass2= request.POST.get('password2')
        if pass1!=pass2:
             return HttpResponse("your password and re-password not same")
        elif User.objects.filter(email=email).exists():
            # return HttpResponse("your password and re-password not same")
            return HttpResponse( " User already exists ")
        else: 
            Register= User.objects.create_user(uname,email,pass1)   
            Register.save()
            return redirect('index.html') 
        
    return render(request,'registration.html')
        
def homelogin(request):
    # message.success(request, "this is succesfull done.")
    if request.method == 'POST':
        username= request.POST.get('username')
        pass1= request.POST.get('password')  
        user=  authenticate(username=username,password=pass1)
        # print(username,pass1)
    
        if user is not None:
            login(request,user)
            return redirect('base.html')
        else:
            messages.warning(request, " Username And password Incorrect " )
            # return HttpResponse(" your password inc ")
            return redirect('login.html')
 
    return render(request,'login.html')  

def logout(request):
    auth.logout(request)
    return redirect('/')


 





 