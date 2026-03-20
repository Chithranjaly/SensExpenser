from django.contrib import admin

from .models import Expenses

# Register your models here.

class AdminExpenses(admin.ModelAdmin):
    list_display = ('title', 'amount', 'category', 'date', 'user')
    list_filter = ('category', 'date', 'user')
admin.site.register(Expenses,AdminExpenses)
