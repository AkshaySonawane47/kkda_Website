# from . import user
# from collections import UserDict
import uuid
from django.db import models 
from django.utils.html import format_html
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from django.contrib.auth.models import User
# from tinymce.models import HTMLField
from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name 

    #catergory model 

class Choreography_Team(models.Model):
    ch_id =models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    description=models.TextField()
    Work_roll =models.CharField(max_length=100)
    image =models.ImageField(upload_to='contents/')
    add_date=models.DateTimeField(auto_now_add=True, null=True)

        
    def __str__(self):
        return self.Name
    

    def image_tag(self):
        return format_html('<img src="{}" style=" width:50; height:30px;"   />'.format(self.image.url))


class slide_image(models.Model):
    cat_id =models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    Price =models.CharField(max_length=100)
    image =models.ImageField(upload_to='contents/')
    add_date=models.DateTimeField(auto_now_add=True, null=True)

        
    def __str__(self):
        return self.title
    

    def image_tag(self):
        return format_html('<img src="{}" style=" width:50; height:30px;"   />'.format(self.image.url))

    #post model
class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content= RichTextField(blank=True,null=True)
    url=models.CharField( max_length=100)
    cat=models.ForeignKey(slide_image, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='post/')
    add_date=models.DateTimeField(auto_now_add=True,auto_now=False, null=True)
    # add_time=models.DateTimeField(auto_now_add=True,auto_now=False)
    post_slug =AutoSlugField(populate_from='title',unique=True,null=True,default=None)
    

    def image_tag(self):
        return format_html('<img src="{}" style=" width:50; height:30px;"   />'.format(self.image.url))

    def __str__(self):
        return self.title
    

    @property
    def cat(self):
        return self.cat
    
    @property
    def cat_id(self):
        return self.cat_id

    # @property
    # def cat_id(self):
    #     return self.C_id



#register form 

class admission_registration(models.Model):
    id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    # Level=models.CharField(max_length=10)
    phone=models.CharField( max_length=15)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    date = models.DateField()

    def __str__(self):
        return self.email
    # class Meta:
    #     table = True


    choose_level = (
        ('Basic','Basic'),
        ('Intermediate','Intermediate'),
        ('Advance','Advance'),

)



class Order_form(models.Model):
    id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    choose_level=models.CharField(max_length=100) 
    phone=models.CharField( max_length=15)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    date = models.DateField()

    # datetime = models.DateTimeField()

  

    def __str__(self):
        return self.choose_level

    
# ------------------------------------------------------------------------------------------------------------------------------------------------  


# class BaseModel(models.Model):
#     uid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
#     created_at= models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         abstract = True


class Dance_Session(models.Model):
    c_level= ( ('basic', 'basic'),
                ('intermadiate','Intermediate'),
                ('Advance','Advance')

    )
    
    # user = models.ForeignKey( on_delete=models.CASCADE )
    Category_name= models.CharField(max_length=100)
    Level = models.CharField(max_length=100 ,choices=c_level )
    price = models.IntegerField()

    def __str__(self):
        return self.Level

class Regular_Batch_Payment(models.Model):
    category= (
            ('dance', 'Dance'),
            ('zumba', 'Zumba'),
            ('music', 'Music')
    )
    level= (
            ('basic', 'Basic'),
            ('intermediate', 'Intermediate'),
            ('advance', 'Advance')
    )
    id=models.AutoField(primary_key=True)
    Student_Name=models.TextField(max_length=100, null=True ) 
    Category =models.CharField(max_length=100, choices=category) 
    Sub_Category =models.CharField(max_length=50, null=True, blank=True , default="Guitar") 
    Level = models.CharField(max_length=100, choices=level)
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name="course" )
    is_paid = models.BooleanField(default=False)
    Offline_payment = models.BooleanField(default=False)
    Online_Payment = models.BooleanField(default=False)
    # order_id = models.CharField(max_length=150)
    paid_Amount = models.IntegerField(null=True, blank=True)
    add_date=models.DateTimeField(auto_now_add=True, null=True)
    Remaining = models.CharField(max_length=10,null=True , blank=True)
    # def __str__(self):
    #     return self.user



# =------------------------------------=====slect field =====-----------------------------------------------------------------------------------------=#



class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()


