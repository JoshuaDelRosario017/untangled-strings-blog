from django.contrib import admin
from untangled.models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.site_header = "Untangled String Admin"
admin.site.site_title = "Untangled String Admin Area"
admin.site.index_title = "Welcome to Untangled String Admin Area"

class BlogAdmin(admin.ModelAdmin):
    list_display = ['blog_id','blog_title','blog_body','blog_pubdate']
    search_fields = ['blog_title']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','blog_categories']

# class CustomUser(admin.ModelAdmin):
#     list_display=['username','fname','lname','password','email']
#     search_fields = ['fname']

class UsersProfile(UserAdmin):
    list_display=['id']

admin.site.register(Blogs, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile)
# admin.site.register(UsersProfile)
