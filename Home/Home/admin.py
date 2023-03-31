import csv
import decimal
from django.db.models import F
from django.contrib import admin
from django.http import HttpResponse
from Home.models import Contact
from Home.models import slide_image
from Home.models import  Post
from Home.models import  Choreography_Team
from Home.models import  admission_registration
from Home.models import  Dance_Session
from Home.models import  Regular_Batch_Payment,form
from Home.models import MultipleImage
from Home.models import gallery_image
from import_export.admin import ImportExportModelAdmin
from .models import Photo, Category, Score ,add_ScoreStudentTable


# @admin.register(Score) 
class ResultAdmin(ImportExportModelAdmin):
    list_display = ('user','score','duration','Attendence','status') 
# class userdata(ImportExportModelAdmin):
    pass 


# from django.contrib.admin import ModelAdmin, register
# from Home.models import home

#
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_id','image_tag_2','title_name','description','Price','add_date')
   

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','message')
    search_fields = ('name',)
    list_per_page = 10

class PostAdmin(admin.ModelAdmin):
    list_display = ('post_id','image_tag','title','add_date')  
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



admin.site.register(Category)
admin.site.register(Photo)


class DanceAdmin(admin.ModelAdmin):
    list_display = ('id','Category_name','Level','price')
    search_fields = ('Category_name',)
    

def export_here(modeladmin, request, queryset):          
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Dance.csv" '
        writer = csv.writer(response)
        writer.writerow(['Student_Name','Category','Level','add_date','paid_Amount','Remaining','is_paid'])
        dance = queryset.values_list('Student_Name','Category','Level','add_date','paid_Amount','Remaining','is_paid')
        for Dance in dance:
            writer.writerow(Dance)
        return response
export_here.short_description =  'Export to csv'

class regularAdmin(admin.ModelAdmin):
    list_display = ('Student_Name','Category','Level','add_date','paid_Amount','Remaining','is_paid')
    search_fields = ('student_name',)
    list_per_page = 5

    actions = ['applay_here',export_here]
    def applay_here(self, request, queryset):
        queryset.update(paid_Amount=F('paid_Amount')*decimal.Decimal('0.9'))
    applay_here.short_description = 'Apply 10%% discount here'  


class orderAdmin(admin.ModelAdmin):
    list_display = ('id','firstname','date',)
    search_fields = ('firstname','id')
  
class ChoreographerAdmin(admin.ModelAdmin):   
    list_display = ('ch_id','Name',)
    search_fields = ('Name',)
class AdminArea(admin.AdminSite):
    site_header = " admin area"

Admin_site =  AdminArea(name='AdminArea')
# Register your models here.
class multiadmin(admin.ModelAdmin):
    list_display = ('image_tag',)

class gallery_imageAdmin(admin.ModelAdmin):
    list_display = ('image_tag','image_category','name_title',) 

class studTableAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user','month','status','Attendence','DanceMarks','StartDate','EndDate') 
    list_per_page = 7
# class userdata(ImportExportModelAdmin):
    pass 
# class ResultAdmin(admin.ModelAdmin):
#     list_display = ('user','score',)
# -------------------------------------------- Register model Here ---------------------------------------------------------------#

admin.site.register(Contact,ContactAdmin)
admin.site.register(slide_image,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(admission_registration,registerAdmin)
admin.site.register(Dance_Session,DanceAdmin)
Admin_site.register(Dance_Session,DanceAdmin)
admin.site.register(Regular_Batch_Payment,regularAdmin)
admin.site.register(Choreography_Team,ChoreographerAdmin)

admin.site.register(gallery_image,gallery_imageAdmin)
admin.site.register(MultipleImage,multiadmin)

admin.site.register(Score,ResultAdmin)
admin.site.register(add_ScoreStudentTable,studTableAdmin)
admin.site.register(form,orderAdmin)


# admin.site.register(MaterialPersonAdmin)


from django.contrib import admin
from embed_video.admin import AdminVideoMixin 
from Home.models import Item

# class ItemAdmin(AdminVideoMixin, admin.ModelAdmin):
#     pass


class ItemAdmin(admin.ModelAdmin):
    
    search_fields = ('video',)
admin.site.register(Item, ItemAdmin)
