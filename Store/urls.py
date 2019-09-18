from django.urls import path
from .views import (StoreListView, StoreDetailView,StoreUpdateView,
					StoreDeleteView,StoreCreateView,
					ManagerDetailView, ManagerUpdateView, ManagerDeleteView,
					EmployeeDetailView,EmployeeCreateView,EmployeeUpdateView,
					EmployeeDeleteView,
					StoreFoodDetailView
					)


urlpatterns = [
	path('', StoreListView.as_view(), name='store-list'),
	path('<int:pk>/', StoreDetailView.as_view(), name='store-detail'),
	path('<int:pk>/foods/<int:food_id>/', StoreFoodDetailView.as_view(), name='store-food-detail'),
	path('add/', StoreCreateView.as_view(), name='store-add'),
	path('<int:pk>/update/', StoreUpdateView.as_view(), name='store-update'),
	path('<int:pk>/delete/', StoreDeleteView.as_view(), name='store-delete'),
	path('manager/<int:pk>/', ManagerDetailView.as_view(), name='manager-detail'),
	path('manager/<int:pk>/update/', ManagerUpdateView.as_view(), name='manager-update'),
	path('manager/<int:pk>/delete/', ManagerDeleteView.as_view(), name='manager-delete'),
	path('<int:pk>/employee/<int:employee_id>/', EmployeeDetailView.as_view(), name='employee-detail'),
	path('employee/<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee-update'),
	path('employee/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee-delete'),
	path('employee/add/', EmployeeCreateView.as_view(), name='employee-add'),


]
