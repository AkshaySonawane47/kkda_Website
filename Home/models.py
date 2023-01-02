from django.db import models
# from matplotlib import category
# from matplotlib import category
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
         return self.name 
#catergory model

# class Category(models.Model):
#     cat_id =models.AutoField(primary_key=True)
#     title=models.CharField(max_length=100)
#     description=models.TextField()
#     url =models.CharField(max_length=100)
#     image =models.ImageField(upload_to='category/')
#     add_date=models.DateTimeField(auto_now_add=True, null=True)


#     #post model
#     class Post(models.Model):
#         post_id=models.AutoField(primary_key=True)
#         title=models.CharField(max_length=100)
#         content=models.TextField()
#         url=models.CharField( max_length=100)
#         cat=models.ForeignKey(category,on_delete=models.CASCADE)
#         image=models.ImageField(upload_to='post/')
