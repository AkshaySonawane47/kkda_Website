from django.contrib import admin
from Home.models import Contact
from Home.models import Category 
from Home.models import  Post

#
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','description','url','add_date')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','message')
    search_fields = ('name',)


# Register your models here.
admin.site.register(Contact,ContactAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post)




