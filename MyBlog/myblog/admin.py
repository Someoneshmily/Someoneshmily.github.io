from django.contrib import admin
from models import *
# Register your models here

# @admin.register(BlogContent)
class BlogContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content','category']

admin.site.register(BlogContent,BlogContentAdmin)
