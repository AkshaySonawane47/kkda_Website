from django.contrib import admin
from Home.models import Contact
from Home.models import Category 
from Home.models import  Post
# from django.contrib.admin import ModelAdmin, register
# from Home.models import home

#
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','url','add_date')
   

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','message')
    search_fields = ('name',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    # list_filter = ('post_id',)  
    list_per_page = 2

# @register(home)
# class MaterialPersonAdmin(ModelAdmin):
#     icon_name = 'Home'



# Register your models here.
admin.site.register(Contact,ContactAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
# admin.site.register(MaterialPersonAdmin)




