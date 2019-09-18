from datetime import datetime
from django.shortcuts import render
from .models import Store, Employee, Manager
from Food.models import Food
from django.urls import reverse_lazy
from django.views.generic import TemplateView,DetailView,ListView, CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from Cart.forms import CartAddFoodForm
from Order.models import Order
from Comment.forms import CommentForm
from Comment.models import Comment
from Food.forms import SearchForm

class HomePageView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['most_sell_foods'] = Food.objects.filter(name__icontains='p')
		context['cheapest_foods'] = Food.objects.filter(price__lte=10)
		context['search_form'] = SearchForm()
		return context


##############################################################
# Store Model Views
##############################################################


class StoreListView(LoginRequiredMixin, ListView):
	model = Store
	context_object_name = 'stores'

class StoreDetailView(LoginRequiredMixin, DetailView):
	model = Store
	context_object_name = 'store'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		store = Store.objects.get(id=self.kwargs['pk'])
		context['foods'] = Food.objects.filter(stores=store).filter(run_out=False)
		context['employees'] = Employee.objects.filter(store__id=self.kwargs['pk'])
		paid_orders = Order.objects.filter(paid=True)
		monthly_income = 0
		for item in paid_orders:
			if item.store_id == self.kwargs['pk']:
				monthly_income += item.get_total_cost()
		context['monthly_income'] = monthly_income
		return context


class StoreCreateView(LoginRequiredMixin, CreateView):
	model = Store
	fields = ['user','manager','foods','branch_num','image','pub_date','address']


class StoreUpdateView(LoginRequiredMixin, UpdateView):
	model = Store
	fields = ['manager','foods','branch_num','image','address']
	context_object_name = 'store'
	template_name = 'Store/store_update_form.html'


class StoreDeleteView(LoginRequiredMixin, DeleteView):
	model = Store
	success_url = reverse_lazy('store-list')
	context_object_name = 'store'


class StoreFoodDetailView(LoginRequiredMixin, DetailView):
	model = Store
	context_object_name = 'store'
	template_name = 'Store/store_food_detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		store = Store.objects.get(id=self.kwargs['pk'])
		food = Food.objects.filter(stores=store).get(id=self.kwargs['food_id'])
		context['food'] = food
		context['cart_food_form'] = CartAddFoodForm()
		context['comment_form'] = CommentForm()
		comments = Comment.objects.filter(food=food)[:5]

		comment_times = []
		now = datetime.now()
		date_format = "%Y-%m-%d  %H:%M:%S"
		time1 = now.strftime("%Y-%m-%d  %H:%M:%S")
		time_now = datetime.strptime(time1,date_format)
		for comment in comments:
			time2 = comment.created.strftime("%Y-%m-%d  %H:%M:%S")
			time_2 = now.strptime(time2,date_format)
			diff_time = time_now - time_2
			if diff_time.days > 0:
				weeks = int(diff_time.days / 7)
				months = int(diff_time.days / 30)
				if months > 0:
					comment_times.append('{} months ago'.format(months))
				else:
					if weeks > 0:
						comment_times.append('{} weeks ago'.format(weeks))
					else:
						comment_times.append('{} days ago'.format(diff_time.days))
			else:
				hours = int(diff_time.seconds / (3600))
				if hours > 0:
					comment_times.append('{} hours ago'.format(hours))
				else:
					minutes = int((diff_time.seconds % 3600) / 60)
					if minutes > 0:
						comment_times.append('{} minutes ago'.format(minutes))
					else:
						comment_times.append('just now')

		food_comments = zip(comments,comment_times)
		context['food_comments'] = food_comments

		self.request.session['store_id'] = store.id

		return context



##############################################################
# Manager Model Views
###############################################################


class ManagerDetailView(LoginRequiredMixin, DetailView):
	model = Manager
	context_object_name = 'manager'



class ManagerUpdateView(LoginRequiredMixin, UpdateView):
	model = Manager
	fields = ['name','address','phone_num','education_degree','image']
	context_object_name = 'manager'
	template_name = 'Store/manager_update_form.html'


class ManagerDeleteView(LoginRequiredMixin, DeleteView):
	model = Manager
	success_url = reverse_lazy('store-list')
	context_object_name = 'manager'


##############################################################
# Employee Model Views
###############################################################



class EmployeeDetailView(LoginRequiredMixin, DetailView):
	model = Employee
	context_object_name = 'employee'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		store_employees = Employee.objects.filter(store_id=self.kwargs['pk'])
		employee = Employee.objects.get(id=self.kwargs['employee_id'])
		if employee in store_employees:
			context['employee'] = employee
		else:
			context['employee'] = None

		return context




class EmployeeCreateView(LoginRequiredMixin, CreateView):
	model = Employee
	fields = ['store','name','address','phone_num','pub_date','image','position','education_degree','monthly_salary']


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
	model = Employee
	fields = ['name','address','phone_num','image','education_degree','position']
	context_object_name = 'employee'
	template_name = 'Store/employee_update_form.html'



class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
	model = Employee
	success_url = reverse_lazy('store-detail')
	context_object_name = 'employee'
