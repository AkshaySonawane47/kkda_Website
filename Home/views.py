from email import message
from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
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
    return render(request, 'index.html')
        
def blog(request):
    # message.success(request, "this is succesfull done.")
    return HttpResponse("this is aboutpage")

def about(request):
    # message.success(request, "this is succesfull done.")
    return render(request,'about.html')
    