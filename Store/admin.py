from django.contrib import admin
from .models import Store, Manager, Employee

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
	list_display = ['name','address','monthly_salary','education_degree','pub_date']
	list_editable = ['address','monthly_salary']
	search_field = ['name','phone_num']

class EmployeeInline(admin.TabularInline):
	model = Employee
	min_num = 1
	extra = 1

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
	inlines = [EmployeeInline]
	search_field = ['address']
	list_display = ['branch_num','manager','address']
	list_editable = ['address']
