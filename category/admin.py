from django.contrib import admin

from .models import Category

class AdminCategory(admin.ModelAdmin):
    list_display = ('user','category_name','description')
    list_filter = ('category_name',)
     
admin.site.register(Category, AdminCategory)
