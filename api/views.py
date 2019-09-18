from rest_framework import generics, permissions, viewsets
from Food.models import Food
from django_filters.rest_framework import DjangoFilterBackend
from Store.models import Store, Employee, Manager
from django.contrib.auth import get_user_model
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from Coupon.models import Coupon
from Order.models import Order
from .serializers import FoodSerializer, StoreSerializer, ManagerSerializer, UserSerializer,CouponSerializer,OrderSerializer


class Pagination(LimitOffsetPagination):
	default_limit = 5
	max_limit = 50

# food api views

class FoodListAPIView(generics.ListCreateAPIView):
	queryset = Food.objects.all()
	serializer_class = FoodSerializer
	filter_backends = (DjangoFilterBackend,SearchFilter,)
	filter_fields = ('name','id',)
	search_fields = ('detail','description',)
	pagination_class = Pagination

class FoodDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Food.objects.all()
	serializer_class = FoodSerializer

# store api views

class StoreListAPIView(generics.ListCreateAPIView):
	queryset = Store.objects.all()
	serializer_class = StoreSerializer
	filter_backends = (DjangoFilterBackend,SearchFilter,)
	filter_fields = ('id','branch_num',)
	search_fields = ('address',)
	pagination_class = Pagination

class StoreDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Store.objects.all()
	serializer_class = StoreSerializer

# manager api views

class ManagerListAPIView(generics.ListCreateAPIView):
	queryset = Manager.objects.all()
	serializer_class = ManagerSerializer
	filter_backends = (DjangoFilterBackend,SearchFilter,)
	filter_fields = ('name',)
	search_fields = ('address','phone_num',)
	pagination_class = Pagination

class ManagerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Manager.objects.all()
	serializer_class = ManagerSerializer


# users api views

class UserListAPIView(generics.ListCreateAPIView):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer
	filter_backends = (DjangoFilterBackend,SearchFilter,)
	filter_fields = ('id',)
	search_fields = ('username',)
	pagination_class = Pagination

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer

# coupons api views
class CouponListAPIView(generics.ListCreateAPIView):
	queryset = Coupon.objects.all()
	serializer_class = CouponSerializer
	filter_backends = (DjangoFilterBackend,SearchFilter,)
	filter_fields = ('code',)
	search_fields = ('code','discount')
	pagination_class = Pagination

class CouponDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Coupon.objects.all()
	serializer_class = CouponSerializer


# orders api views
class OrderListAPIView(generics.ListCreateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	filter_backends = (DjangoFilterBackend,SearchFilter,)
	filter_fields = ('name','address','city')
	search_fields = ('address','store_id','discount','paid')
	pagination_class = Pagination

class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
