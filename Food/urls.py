from django.urls import path
from .views import FoodListView, FoodDetailView, FoodCreateView, FoodUpdateView, FoodDeleteView


urlpatterns = [
	path('', FoodListView.as_view(), name='food-list'),
	path('<int:pk>/', FoodDetailView.as_view(), name='food-detail'),
	path('add/', FoodCreateView.as_view(), name='food-add'),
	path('<int:pk>/delete/', FoodDeleteView.as_view(), name='food-delete'),
	path('<int:pk>/update/', FoodUpdateView.as_view(), name='food-update'),

]
