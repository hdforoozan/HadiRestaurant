"""hadirestaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Store.views import HomePageView
from Food.views import search_food


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('Account.urls')),
    path('foods/', include('Food.urls')),
    path('stores/', include('Store.urls')),
    path('cart/', include('Cart.urls')),
    path('coupons/', include('Coupon.urls')),
    path('comments/', include('Comment.urls')),
    path('orders/', include('Order.urls')),
    path('', HomePageView.as_view(), name='home'),
    path('search/', search_food, name='search'),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    #path('api/v1/socialaccounts/', include('allauth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('social-auth/',include('social_django.urls', namespace='social')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

