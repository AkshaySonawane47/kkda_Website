from django.contrib import admin
from Home.models import Contact
from Home.models import Category 
from Home.models import  Post
from Home.models import  admission_registration
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

# Register your models here.
admin.site.register(Contact,ContactAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(admission_registration,registerAdmin)
# admin.site.register(MaterialPersonAdmin)




