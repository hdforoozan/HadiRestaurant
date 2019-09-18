from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth','address','phone_num']
    list_editable = ['address','phone_num']
    list_filter = ['user','phone_num']
