from django.contrib import admin
from Home.models import Contact
from Home.models import slide_image
from Home.models import  Post
from Home.models import  admission_registration
from Home.models import  Dance_Session
from Home.models import  purchase,Order_form


# from django.contrib.admin import ModelAdmin, register
# from Home.models import home

#
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','Price','add_date')
   

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','message')
    search_fields = ('name',)
    list_per_page = 10

class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','add_date')  
    search_fields = ('title',)
    # list_filter = ('post_id',)  
    list_per_page = 4

# @register(home)
# class MaterialPersonAdmin(ModelAdmin):
#     icon_name = 'Home'

class registerAdmin(admin.ModelAdmin):
    list_display = ('id','firstname','address','date')  
    search_fields = ('firstname',)
    # list_filter = ('post_id',)  
    list_per_page = 5



class DanceAdmin(admin.ModelAdmin):
    list_display = ('id','Category_name','Level','price')
    search_fields = ('Category_name',)
    
class purchesAdmin(admin.ModelAdmin):
    list_display = ('id','user','add_date')
    search_fields = ('user',)
  
class orderAdmin(admin.ModelAdmin):
    list_display = ('id','firstname',)
    search_fields = ('firstname',)
  

# -------------------------------------------- Register model Here ---------------------------------------------------------------#



# Register your models here.

admin.site.register(Contact,ContactAdmin)
admin.site.register(slide_image,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(admission_registration,registerAdmin)
admin.site.register(Dance_Session,DanceAdmin)
admin.site.register(purchase,purchesAdmin)


admin.site.register(Order_form,orderAdmin)


# admin.site.register(MaterialPersonAdmin)


