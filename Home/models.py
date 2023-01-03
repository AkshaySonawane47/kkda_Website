from django.db import models 
from django.utils.html import format_html
from ckeditor.fields import RichTextField

# from tinymce.models import HTMLField


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name 

    #catergory model

class Category(models.Model):
    cat_id =models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    url =models.CharField(max_length=100)
    image =models.ImageField(upload_to='contents/')
    add_date=models.DateTimeField(auto_now_add=True, null=True)


    def image_tag(self):
        return format_html('<img src="{}" style=" width:50; height:30px;"   />'.format(self.image.url))
        
    def __str__(self):
        return self.title
    

    #post model
class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content= RichTextField(blank=True,null=True)
    url=models.CharField( max_length=100)
    cat=models.ForeignKey(Category, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='post/')

    def __str__(self):
        return self.title

    @property
    def cat(self):
        return self.cat
    
    @property
    def cat_id(self):
        return self.cat_id
    