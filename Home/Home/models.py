# from . import user
# from collections import UserDict

from django.db import models 
from django.utils.html import format_html
# from ckeditor.fields import RichTextField
from tinymce.models import HTMLField

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
    title_name=models.CharField(max_length=100)
    description=models.TextField()
    Price =models.CharField(max_length=100)
    image =models.ImageField(upload_to='contents/')
    add_date=models.DateTimeField(auto_now_add=True, null=True)

    @property
    def __str__(self):
        return self.title_name
    

    def image_tag_2(self):
        return format_html('<img src="{}" style=" width:50; height:30px;"   />'.format(self.image.url))



# GALLERY IMAGE'S
class gallery_image(models.Model):


    cat = (
        ('Celebrity_workshop','Celebrity_workshop'),
        ('Garba_workshop','Garba_workshop_&_Navaratri_event'),
        ('Yearly_festival','Yearly_festival'),   
        ('Achievement','Achievement'),  
    )
    
   
    # id= models.AutoField(primary_key=True)
    image_category=models.CharField(max_length=100, choices=cat)
    name_title = models.TextField(max_length=100 )
    image_upload= models.ImageField(upload_to='contents/')
    # event_Category= models.ImageField(max_length=50)  
    date = models.DateTimeField(auto_now=False, auto_now_add=False) 
    
    # @property
    def __str__(self):
        return self.name_title
    

    def image_tag(self):
        return format_html('<img src="{}" style=" width:50; height:30px;"   />'.format(self.image_upload.url))





    #post model 
class Post(models.Model):

    # cat = (
    #     ('selebrity','selebrity'),
    #     ('Garba','Garba'),
    #     ('Achivement','Achivement'), 
    #     ('Yealy_festival','Year_festival'),  
    #     )

    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content= HTMLField()
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
        return self.date
    # class Meta:
    #     table = True


#     choose_level = (
#         ('Basic','Basic'),
#         ('Intermediate','Intermediate'),
#         ('Advance','Advance'),

# )



class form(models.Model):
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

    

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
    
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description




    # from django.db import models
class MultipleImage(models.Model):
    image = models.ImageField(upload_to='contents/') 
    # photo = models.ImageField(upload_to ='photos/')

    def image_tag(self):
        return format_html('<img src="{}" style=" width:90; height:50px;"   />'.format(self.image.url))
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


# class Dance(models.Model):
   
#     plan= models.CharField(max_length=100)
#     user = models.ForeignKey(User, on_delete=models.CASCADE , related_name="course" )
#     is_paid = models.BooleanField(default=False)
   
#     def __str__(self):
#         return self.plan


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
    
    def __str__(self):
        return self.add_date



# =------------------------------------=====slect field =====-----------------------------------------------------------------------------------------=#



class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()



# class Result(models.Model):
    
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     test_name = models.CharField(max_length=50)
#     score = models.IntegerField()


class Score(models.Model):

    st = (
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Average','Average'),
        ('Low','Low') ,
        ('you are terminated', 'you are terminated')
    )

    du = (
        
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    duration = models.CharField(max_length=50)
    Attendence = models.IntegerField(null=True, blank=True)
    status = models.TextField(max_length=50 ,choices=st)
    month = models.CharField(max_length=20, default="January")
    Total_days = models.IntegerField( default="31")
    score = models.IntegerField()


class add_ScoreStudentTable(models.Model):

    st = (
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Average','Average'),
        ('Low','Low') ,
        ('you are terminated', 'you are terminated')
    )

    du = (
        
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    month = models.CharField(max_length=20, default="January")
    status = models.TextField(max_length=50 ,choices=st)
    Attendence = models.IntegerField(null=True, blank=True)
    Total_days = models.IntegerField( default="31")
    DanceMarks = models.IntegerField(default="/20")
    score = models.IntegerField()
    duration = models.CharField(max_length=50)
    # date= models.DateField( auto_now=False, auto_now_add=False)
    StartDate=models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    EndDate = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True) 
   


