from email import message
from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from Home.models import  Post,Category
from django.contrib import messages


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

        
def blog(request):
    # message.success(request, "this is succesfull done.")
    return HttpResponse("this is aboutpage")  

def about(request):
    # message.success(request, "this is succesfull done.")
    return render(request,'about.html')
    
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
