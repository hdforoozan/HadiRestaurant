# api/urls.py
from django.urls import path
from .views import (FoodListAPIView, FoodDetailAPIView, StoreListAPIView,
		StoreDetailAPIView, ManagerListAPIView, ManagerDetailAPIView,
		UserListAPIView, UserDetailAPIView,
		CouponListAPIView,CouponDetailAPIView,
		OrderListAPIView,OrderDetailAPIView)

urlpatterns = [
	path('foods/', FoodListAPIView.as_view()),
	path('foods/<int:pk>/', FoodDetailAPIView.as_view()),
	path('stores/', StoreListAPIView.as_view()),
	path('stores/<int:pk>/', StoreDetailAPIView.as_view()),
	path('managers/', ManagerListAPIView.as_view()),
	path('managers/<int:pk>/', ManagerDetailAPIView.as_view()),
	path('users/', UserListAPIView.as_view()),
	path('users/<int:pk>/', UserDetailAPIView.as_view()),
	path('coupons/', CouponListAPIView.as_view()),
	path('coupons/<int:pk>/', CouponDetailAPIView.as_view()),
	path('orders/', OrderListAPIView.as_view()),
	path('orders/<int:pk>/', OrderDetailAPIView.as_view()),
]
