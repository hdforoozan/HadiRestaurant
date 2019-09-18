from django.urls import path
from . import views


urlpatterns = [
    path('submit/<int:store_id>/<int:food_id>/', views.submit_comment , name='submit-comment')
]
