from rest_framework import serializers
from django.contrib.auth import get_user_model
from Account.models import Profile
from Food.models import Food
from Store.models import Store, Manager, Employee
from Coupon.models import Coupon
from Order.models import Order,OrderItem
from Comment.models import Comment

class FoodSerializer(serializers.ModelSerializer):
	pub_date = serializers.DateTimeField(
		input_formats = ['%I:%M %p %d %B %Y'], format=None, allow_null=True,
		help_text='Accepted format is : "12:02 PM 17 April 2019"',
		style={'input_type':'text', 'placeholder':'12:07 PM 12 July 2019'}
		)
	class Meta:
		model = Food
		fields = ['id','user','name','description','image','pub_date','price','detail']

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = ['id','name','address','phone_num','education_degree',
		'image','position','monthly_salary','pub_date']

class StoreSerializer(serializers.ModelSerializer):
	employees = EmployeeSerializer(many=True, read_only=True)
	foods = FoodSerializer(many=True, read_only=True)
	pub_date = serializers.DateTimeField(
		input_formats = ['%I:%M %p %d %B %Y'], format=None, allow_null=True,
		help_text='Accepted format is : "12:02 PM 17 April 2019"',
		style={'input_type':'text', 'placeholder':'12:07 PM 12 July 2019'}
		)

	class Meta:
		model = Store
		fields = ['id','user', 'manager','foods','branch_num',
		'image','pub_date','address', 'employees']


class ManagerSerializer(serializers.ModelSerializer):
	pub_date = serializers.DateTimeField(
		input_formats = ['%I:%M %p %d %B %Y'], format=None, allow_null=True,
		help_text='Accepted format is : "12:02 PM 17 April 2019"',
		style={'input_type':'text', 'placeholder':'12:07 PM 12 July 2019'}
		)

	class Meta:
		model = Manager
		fields = ['id','name','address','phone_num','pub_date']

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ['date_of_birth','photo','address','phone_num','credit']

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ['comment','food','created']

class UserSerializer(serializers.ModelSerializer):
	user_comments = CommentSerializer(many=True, read_only=True)
	profile = ProfileSerializer(read_only=True)
	class Meta:
		model = get_user_model()
		fields = ['id','username','user_comments','profile']


class CouponSerializer(serializers.ModelSerializer):
	valid_from = serializers.DateTimeField(
		input_formats = ['%I:%M %p %d %B %Y'], format=None, allow_null=True,
		help_text='Accepted format is : "12:02 PM 17 April 2019"',
		style={'input_type':'text', 'placeholder':'12:07 PM 12 July 2019'}
		)
	valid_to = serializers.DateTimeField(
		input_formats = ['%I:%M %p %d %B %Y'], format=None, allow_null=True,
		help_text='Accepted format is : "12:02 PM 17 April 2019"',
		style={'input_type':'text', 'placeholder':'12:07 PM 12 July 2019'}
		)
	class Meta:
		model = Coupon
		fields = ['id','code','discount','valid_from','valid_to','active']

class OrderItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderItem
		fields = ['food','price','quantity']

class OrderSerializer(serializers.ModelSerializer):
	items = OrderItemSerializer(many=True, read_only=True)
	created = serializers.DateTimeField(
		input_formats = ['%I:%M %p %d %B %Y'], format=None, allow_null=True,
		help_text='Accepted format is : "12:02 PM 17 April 2019"',
		style={'input_type':'text', 'placeholder':'12:07 PM 12 July 2019'}
		)
	updated = serializers.DateTimeField(
		input_formats = ['%I:%M %p %d %B %Y'], format=None, allow_null=True,
		help_text='Accepted format is : "12:02 PM 17 April 2019"',
		style={'input_type':'text', 'placeholder':'12:07 PM 12 July 2019'}
		)
	class Meta:
		model = Order
		fields = ['id','name','address','city','created',
		'updated','paid','discount','store_id','items']
