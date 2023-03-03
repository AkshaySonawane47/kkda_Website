from email import message

from kkda_website.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
from . import models
from django.shortcuts import render, HttpResponse , redirect
from datetime import datetime
from Home.models import Contact, Order_form, admission_registration 
from Home.models import  Post,slide_image
from Home.models import  Choreography_Team
from django.contrib import messages
# from Home.models import admission_registration 
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator 
from instamojo_wrapper import Instamojo
from django.conf import settings
import requests
import razorpay
from .models import Item  






  
# api = Instamojo(api_key=settings.API_KEY,
#     auth_token= settings.AUTH_TOKEN, endpoint= 'https://test.instamojo.com/api/1.1/'
#     )

# api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')

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
    cat=slide_image.objects.all()
    choreographer=Choreography_Team.objects.all()
    
    data={  'post': post ,
            'cat': cat ,
            'choreographer': choreographer,
       } 
    return render(request, 'index.html',data)




def gallery(request):

    return render(request,'gallery.html')





def about(request):
    # message.success(request, "this is succesfull done.")
    return render(request,'about.html')


# @login_required(login_url='login') 
def base(request):
    # message.success(request, "this is succesfull done.")
  
    if request.method == "POST":
        select = request.POST.get('select')
        # select= request.POST.get('select')
        # select=request.POST.get('select')
        if  select=='dance':
            return redirect('Category/dance.html')
        elif select=='zumba':
             return redirect('Category/music.html')
        elif select=='music':
             return redirect('Category/music.html')
             
        elif select=='wedding':
             return redirect('Category/wedding.html')
        elif select=='costume':
             return redirect('Category/costume.html')
        elif select=='personal':
             return redirect('Category/personal_choreography.html')
        else:
            return render(request,'base.html')

    obj=Item.objects.all()

    return render(request,'base.html',{'obj':obj})

    # return render(request,'base.html')
    # message.success(request, "this is succesfull done.")

# def posts(request,id):
#     pots = Post.objects.get(post_id=id)
#     posts = Post.objects.filter(url=pots)
#     context = { 'pots': pots, 'posts': posts}
#     return render(request,'posts.html', context)    

@login_required(login_url='login')
def dance(request):
    # message.success(request, "this is succesfull done.")
    return render(request,'Category/dance.html') 

@login_required(login_url='login')
def music(request):
    # message.success(request, "this is succesfull done.")
    return render(request,'Category/music.html')

@login_required(login_url='login')
def wedding(request):
    # message.success(request, "this is succesfull done.")
    return render(request,'Category/wedding.html') 

@login_required(login_url='login')
def zumba(request):
    # message.success(request, "this is succesfull done.")
    return render(request,'Category/zumba.html') 

@login_required(login_url='login')
def costume(request):
    # message.success(request, "this is succesfull done.")
    return render(request,'Category/costume.html') 

@login_required(login_url='login')
def personal_choreography(request):
    # message.success(request, "this is succesfull done.")
    return render(request,'Category/personal_choreography.html') 


client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

@login_required(login_url='login')
def checkout(request):
    # import razorpay

    DATA = {
        'amount': 50000,
        'currency': 'INR',
        'payment_capture': 1,
        # "notes": {    
        #     "key1": "rzp_test_cFFpCNmI0yg0an",
        #     "key2": "gKOQi6eDtEn3nJD0EBnWvZJy"
        # }
    }
    payment_order = client.order.create(data=DATA)
    payment_order_id = payment_order['id']
    Basic =  {
        'amount': 500 , 'api_key': RAZORPAY_API_KEY, 'order_id': payment_order_id
    }
    # message.success(request, "this is succesfull done.")
    return render(request,'Category/checkout.html',Basic) 


@login_required(login_url='login')
def home_2(request):
    page = request.GET.get('page')
    post=Post.objects.all()
    Paginators= Paginator(post,2)
    final = Paginators.get_page(page)
    totalpage =final.paginator.num_pages
    upload={  'post':final,'lastpage':totalpage,'totalpagelist':[n+1 for n in range(totalpage)] } 
    
    # message.success(request, "this is succesfull done.")
    return render(request,'home_2.html',upload) 


@login_required(login_url='login')
def demo1(request):
    # message.success(request, "this is succesfull done.")
    return render(request,'demo1.html') 


# def base(request):
#     # message.success(request, "this is succesfull done.")

#     post=Post.objects.all()
#     data={  'post': post    }


def submit_form(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        middlename = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        gender = request.POST.get('gender') 
        # Level = request.POST.get('Level') 
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        email = request.POST.get('email')
        # print(Level)
        if  User.objects.filter(email=email).exists():

            messages.warning(request, "you are alredy submited form please Create New One and Use differnt Email id ") 
            return redirect('demo1.html')
        else:
            print(firstname,middlename,lastname,gender,phone,address,email)
            messages.success(request, "Registration Successfully Done! Thank You") 
            msg = "Congratulation, Team will contacting you sortly! " 
            submit_form=admission_registration(firstname=firstname,middlename=middlename,lastname=lastname,gender=gender,phone=phone,address=address,email=email, date = datetime.today())
            submit_form.save()
            return render(request,'demo1.html',{'msg': msg})
    # else:
        # return HttpResponse("404 - not found")
    return render(request,'demo1.html')
    
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
            return redirect('login.html') 
        
    return render(request,'registration.html') 

# @login_required(login_url='login') 
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


 
def password_change(request):
    user =request.user
    form = SetPasswordForm(user) 
    return render(request,'password_reset_confirm.html',{'form':form}) 


# def order(request,id):

#     try:
#         product_obj = Dance_Session.objects.get(id=id)
#         order_obj, _ = purchase.objects.get_or_create(
#             product = product_obj,
#             user = request.user,
#             is_paid = False

#         )
#         return render(request,'Category/order.html')

#     except Exception as e :
#         print(e)




@login_required(login_url='login')
def order(request):
    # plandetail=models.Dance_Session.objects.get(post_id=id)
    # message.success(request, "this is succesfull done.")
    # product_obj = Dance_Session.objects.get()
    # order_obj, _ = purchase.objects.get_or_create(
    #   product = product_obj,
    #     user= request.user,
    #     is_paid = False,  
    # )
        

    # response = requests.get(
    # "https://api.instamojo.com/v2/payment_requests/9ef9b530ff8e440dbbc29f2157bc69ad/",  
    # )   
    # payload = {
    # 'id': '9c337d3c5e3242fca818937366b915b4',
    # }
    # response = requests.post(
    # "https://api.instamojo.com/v2/gateway/orders/payment-request/", 
    # data=payload,
    # )
#
    # response = api.payment_request_create( 
    #     purpose= 'FIFA 16',   
    #     amount= 33,
    #     send_email= True,
    #     buyer_name= 'akshay sonawane',
    #     email= 'akshay.kkda@gmail',
    #     redirect_url= 'http://127.0.0.1:8000/pay_success'
    # )
    # print(response)
    # order_obj = response['payment_request']['id']
    # order_obj.save()

    # print the long URL of the payment request.
    # response['payment_request']['longurl']
    # print the unique ID(or payment request ID)
    # response['payment_request']['id']
    
    
    return render(request,'Category/order.html')
        # print the long URL of the payment request.
            # response['payment_request']['longurl']
            # print the unique ID(or payment request ID)
                # response['payment_request']['id']



# stripe.api_key = 'sk_test_51Mbb3XSBFpVSIJRAW4YLBzE4ZOaDYKSYNHSh0ZJc5mf6TKQ0kqZ3W0LRoB4T7LwUPC8oLmCdJBQLNx1zSRt105RT00E8FtB1NV'


# def checkout_session(request,plan_id):
#     plan=models.Dance_Session.object.get(pk=plan_id)
#     session = stripe.checkout.Session.create(
#         line_items=[{
#         'price_data': {
#             'currency': 'inr',
#             'product_data': {
#             'name': 'plan.Category_name',
#             },
#             'unit_amount': 22, 
#         },
#         'quantity': 1,
#         }],
    
#         mode='payment',
#         success_url='http://127.0.0.1:8000//pay_success',
#         cancel_url='http://127.0.0.1:8000//pay_cancel',

#   )

#     return redirect(session.url, code=303)


def pay_success(request):
    # message.success(request, "this is succesfull done.") 
    return render(request,'Category/success.html') 
def pay_cancel(request):
    # message.success(request, "this is succesfull done.")
    return render(request,'Category/cancel.html') 





def order_form(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        middlename = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        gender = request.POST.get('gender') 
        choose_level = request.POST.get('choose_level') 
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        email = request.POST.get('email')
        # print(Level)
        if User.objects.filter(email=email).exists():
            # return HttpResponse("your password and re-password not same")
            # return HttpResponse( " User already exists ")
            messages.warning(request, "you are alredy submited form please Create New One and Use differnt Email id ") 
            return redirect('Category/order.html')
        else: 
            print(firstname,middlename,lastname,gender,choose_level,phone,address,email)
            messages.success(request, "Registration Successfully Done! Thank You") 
            # msg = "Congratulation, Team will contacting you sortly! " 
            submit_form= Order_form(firstname=firstname,middlename=middlename,lastname=lastname,gender=gender,choose_level=choose_level,phone=phone,address=address,email=email,date=datetime.today())
            submit_form.save()
            return render(request,'Category/order.html')
            # ,{'msg': msg})
        
            # return redirect('demo1.html')
      
    # else:
        # return HttpResponse("404 - not found")
    return render(request,'Category/order.html')


 