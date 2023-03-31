from email import message
import json
# from os import login_tty
from kkda_website.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
from . import models
from django.shortcuts import render, HttpResponse , redirect
from datetime import datetime
from Home.models import Contact, form, admission_registration 
from Home.models import  Post,slide_image
from Home.models import Photo , Category ,gallery_image
from Home.models import  Choreography_Team
from django.contrib import messages
# from Home.models import admission_registration 
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator , PageNotAnInteger
from instamojo_wrapper import Instamojo
from django.conf import settings
import requests
import razorpay
from .models import Item, Regular_Batch_Payment, Score  , add_ScoreStudentTable
import stripe
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
 
# from cashfree_sdk.payouts.client import Client

# client = Client(app_id="YOUR_APP_ID", secret_key="YOUR_SECRET_KEY")

from django.views.decorators.http import require_POST

@csrf_exempt
@require_POST
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, stripe.api_key 
        )
    except ObjectDoesNotExist as e:
        # Invalid payload
        return HttpResponse("payment is not made")
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse("payment is maded")

    if event['type'] == 'payment_intent.payment_failed':
        # Handle the case where the payment fails
        # Update your application accordingly
        return HttpResponse(status=200)

    # Handle other webhook events
    # Update your application accordingly

    return HttpResponse(status=200)


def course(request,cid):
    return HttpResponse(cid)


# --------------------#-------------------------------#------------------------------#===========
# def initiate_payment(request):


@csrf_exempt
def charge(request):
  
    return render(request, 'charge.html')
# Add a success page to your 

def pay(request):

    return redirect(request,'')

def home(request):  
    try:
        if request.method == "POST":
            name = request.POST.get('name')
            email= request.POST.get('email')
            message=request.POST.get('message')
            home = Contact(name=name, email=email, message=message, date = datetime.today())
            home.save()
            messages.success(request, "Your Contact Message has been Sent ! Thank You " +name )
            # messages.success(request, 'Your Contact Message has been Sent!')
        
        
        # data = {'post_s': post_s }
        post=Post.objects.all()
        cat=slide_image.objects.all()
        choreographer=Choreography_Team.objects.all()
        
        data={  'post': post ,
                'cat': cat ,
                'choreographer': choreographer,
        } 
    except ObjectDoesNotExist: 
         return render(request, 'index.html')
    else:
         return render(request, 'index.html',data)




def zumba(request):

    return render(request,'Category/zumba.html')



def construction(request):
    # message.success(request, "this is succesfull done.")
    return render(request,'Category/construction.html')


def about(request):
    # message.success(request, "this is succesfull done.")
    return render(request,'about.html')


@login_required(login_url='login.html') 
def base(request):
    # message.success(request, "this is succesfull done.")
  
    if request.method == "POST":
        select = request.POST.get('select')
        # select= request.POST.get('select')
        # select=request.POST.get('select')
        if  select=='dance':
            return redirect('Category/dance.html')
        elif select=='zumba':
             return redirect('Category/zumba.html')
        elif select=='music':
             return redirect('Category/music.html')
             
        elif select=='wedding':
             return redirect('Category/wedding.html')
        elif select=='costume':
             return redirect('Category/costume.html')
        elif select=='personal':
             return redirect('Category/construction.html')
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

@login_required(login_url='login.html')
def dance(request):
    # message.success(request, "this is succesfull done.")
    return render(request,'Category/dance.html') 

@login_required(login_url='login.html')
def music(request):
    # message.success(request, "this is succesfull done.")
    return render(request,'Category/music.html')

@login_required(login_url='login.html')
def wedding(request):
    # message.success(request, "this is succesfull done.")
    return render(request,'Category/wedding.html') 

@login_required(login_url='login.html')
def gallery(request):

    photos= gallery_image.objects.all()
    
    data={  
            'photos': photos
       } 

    # message.success(request, "this is succesfull done.")
    return render(request,'Category/gallery.html',data) 


@login_required(login_url='login.html')
def score(request):
    try:
        score = Score.objects.get(user=request.user)
        Add_score= add_ScoreStudentTable.objects.filter(user=request.user)
        # data = Add_score.all()
        # Add_score= add_ScoreStudentTable.objects.get(user=request.user)
        Paginators= Paginator(Add_score,12)
        page = request.GET.get('page')
        final = Paginators.get_page(page)  
        totalpage =final.paginator.num_pages 
        upload={'Add_score': Add_score, 'score': score, 'Add_score':final,'lastpage':totalpage,'totalpagelist':[n+1 for n in range(totalpage)] } 
    except ObjectDoesNotExist:  
    # return render(request, 'Category/score.html', {'score': score , 'Add_score': Add_score})
        return render(request, 'category/score.html' )

    else:
        return render(request, 'category/score.html' ,upload)




@login_required(login_url='login.html')
def costume(request):
    # message.success(request, "this is succesfull done.")
    return render(request,'Category/costume.html') 

@login_required(login_url='login.html')
def personal_choreography(request):
    # message.success(request, "this is succesfull done.")
    return render(request,'Category/personal_choreography.html') 


client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

@login_required(login_url='login.html')
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


@login_required(login_url='login.html')
def home_2(request):
    page = request.GET.get('page')
    post=Post.objects.all() 
    Paginators= Paginator(post,2)
    final = Paginators.get_page(page)
    totalpage =final.paginator.num_pages
    upload={  'post':final,'lastpage':totalpage,'totalpagelist':[n+1 for n in range(totalpage)] } 
    
    # message.success(request, "this is succesfull done.")
    return render(request,'home_2.html',upload) 


@login_required(login_url='login.html')
def demo1(request):
    # message.success(request, "this is succesfull done.")
    return render(request,'demo1.html') 

    # message.success(request, "this is succesfull done.")

@login_required(login_url='login.html')
def photo(request):
    user = request.user

    categories = user.category_set.all()

    if request.method == 'POST':
        data = request.POST 
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                user=user,
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(  
                category=category,
                description=data['description'],
                image=image, 
            )

        return redirect('gallery.html')

    context = {'categories': categories}
    return render(request, 'upload_photo.html', context) 


@login_required(login_url='login.html')
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

@login_required(login_url='login.html')
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




@login_required(login_url='login.html')
def order(request):
  
    
    return render(request,'Category/order.html')


if __name__== '__main__':
    home.run(port=4242)

def pay_success(request):
    
    ch=Regular_Batch_Payment.objects.all()
    
    data={  
            'ch': ch,
       } 
    # message.success(request, "this is succesfull done.") 
    return render(request,'Category/success.html',data) 

def pay_cancel(request):
    # message.success(request, "this is succesfull done.")
    return render(request,'Category/cancel.html') 

@login_required(login_url='login.html')
def form(request):
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
            submit_form= form(firstname=firstname,middlename=middlename,lastname=lastname,gender=gender,choose_level=choose_level,phone=phone,address=address,email=email,date=datetime.today())
            submit_form.save()
            return render(request,'Category/order.html')
            # ,{'msg': msg})
        
            # return redirect('demo1.html')
      
    # else:
        # return HttpResponse("404 - not found")
    return render(request,'Category/order.html') 


 



#___________{{============}{{{{{{{{{{============================}{{{{{{{{{{{{{{{{{{{{{{==============================}}}}}}}}}}}}}}}{===================}}}}}}}}}}}}}}}}}}=======================_______________#

# `````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

import stripe


stripe.api_key = 'sk_test_51Mbb3XSBFpVSIJRAW4YLBzE4ZOaDYKSYNHSh0ZJc5mf6TKQ0kqZ3W0LRoB4T7LwUPC8oLmCdJBQLNx1zSRt105RT00E8FtB1NV'


price = stripe.Price.create(
    unit_amount=1000,
    currency='inr',
    product='prod_NW6ZDflbCBhRJF',
)

price_id = price.id

# @app.route('/create-checkout-session', methods=['POST'])

@login_required(login_url='login.html')
def create_checkout_session(request):
    # plan=models.Dance_Session.object.get()
   
    # price = 1000  # $10.00

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
           'price': 'price_1Ml4M4SBFpVSIJRA26MCKGtj',
          'quantity': 1,
        #   'unit_amount': 5000,
        }],
        metadata={
            'price_id': 'your_custom_price_id',
        },
        mode='subscription',
        success_url='http://127.0.0.1:8000/pay_success',
        cancel_url='http://127.0.0.1:8000/pay_cancel',

  )

    return redirect(session.url, code=303)

# -----------------------------------------------------------------------------------------------------------------------------------------------

price = stripe.Price.create(
    unit_amount=1000,
    currency='inr',
    product='prod_NW6ZDflbCBhRJF',
)

price_id = price.id


# @app.route('/create-checkout-session', methods=['POST'])
def checkout_Dance_basic_batch (request):

    try: 
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
            'price': 'price_1Ml4M4SBFpVSIJRA26MCKGtj',
            'quantity': 1,
            #   'unit_amount': 5000,
            }],
            metadata={
                'price_id': 'your_custom_price_id',
            },
            mode='subscription',

            success_url='http://127.0.0.1:8000/pay_success',
            cancel_url='http://127.0.0.1:8000/pay_cancel',

        )
    except ObjectDoesNotExist as e:
    #     # Invalid payload
        return redirect(request, "Category/wedding.html")
    else:
        return redirect(session.url, code=303)
        
# import stripe
# from django.shortcuts import render, redirect
# from django.conf import settings

# stripe.api_key = settings.STRIPE_SECRET_KEY


# -------------------------------------------------------------------------------------------------------------------------------------

# def create_checkout_sess(request):
#     if request.method == 'POST':
#         # Get the subscription plan ID from the form data
#         plan = request.POST.get['plan']

#         # message=request.POST.get('message')
#         home = Dance(plan=plan, date = datetime.today())
#         home.save()
#         messages.success(request, "Your Contact Message has been Sent ! Thank You " +User )
#         # messages.success(request, 'Your Contact Message has been Sent!')
    
#         # Create a new checkout session with the chosen subscription plan
#         checkout_session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             subscription_data={
#                 'items': [{
#                     'plan': plan,
#                 }],
#             },
#             success_url='http://127.0.0.1:8000/pay_success',
#             cancel_url='http://127.0.0.1:8000/pay_cancel',
#         )

#         # Redirect the user to the checkout page
#         return redirect(checkout_session.url)
#     else:
#         # Render the subscription plans page with the available plans
#         plans = stripe.Plan.list()
#         return render(request, 'pay_success.html', {'plans': plans})




# ===============================================================================================================================================




# price = stripe.Price.create(
#     unit_amount=1000,
#     currency='inr',
#     product='prod_NWZahtCAdG2HA7',
# )

price = stripe.Price.create(
    unit_amount=1000,
    currency='inr',
    product='prod_NW6ZDflbCBhRJF',  
)

price_id = price.id
# @app.route('/create-checkout-session', methods=['POST'])
def checkout_intermediate_batch(request):
    # plan=models.Dance_Session.object.get(h2)
   
    # price = 1000  # $10.00
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'quantity': 1,
            'price': 'price_1Ml4M4SBFpVSIJRA26MCKGtj',
          
        }],
        metadata={
            'price_id': 'your_costum_price_id',   
        },
        mode='subscription',
        allow_promotion_codes=True,
        success_url='http://127.0.0.1:8000/pay_success',
         cancel_url='http://127.0.0.1:8000/pay_cancel', 
  )
    return redirect(session.url)

# stripe.api_key = settings.STRIPE_SECRET_KEY


# stripe.PromotionCode.create(coupon="{{COUPON_ID}}", code="VIPCODE")

def customer_portal(request):
# if  ('/create-customer-portal-session',
 if request.method == 'POST':
  # Authenticate your user.
  session = stripe.billing_portal.Session.create(
    # customer=''
    return_url='http://127.0.0.1:8000/pay_successt',
  )
  return redirect(session.url)



def create_order(request):

    return HttpResponse('hello motto') 




# from .models import Result

# def user_results(request):
#     # result = User.objects.get(admin=request.user.id)
#     # results = Result.objects.filter(stud_id=result.id) 
#     # user = request.User  
#     results = Result.objects.filter(request.user)
#     return render(request, 'costume.html', {'results': results})

# def score(request):
   