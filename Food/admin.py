from django.contrib import admin
from .models import Food

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name','price','pub_date','run_out']
    list_editable = ['price','run_out']
    list_filter = ['id','name']
    search_fields = ['name','detail','description']
