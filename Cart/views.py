from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from Food.models import Food
from Store.models import Store
from .forms import CartAddFoodForm
from .cart import Cart
from Coupon.forms import CouponForm

@require_POST
@login_required
def cart_add(request, food_id, store_id):
    cart = Cart(request)
    food = get_object_or_404(Food,id=food_id)
    form  = CartAddFoodForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(food= food, store_id= store_id, quantity= cd['quantity'], update_quantity= cd['update'])

    return redirect('cart_detail')

@login_required
def cart_remove(request, food_id):
    cart = Cart(request)
    food = get_object_or_404(Food, id=food_id)
    cart.remove(food)
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart = Cart(request)
    store_id = cart.get_store_id()
    coupon_form = CouponForm()
    for item in cart:
        item['update_quantity_form'] = CartAddFoodForm(
        initial={'quantity': item['quantity'], 'update': True}
        )
    return render(request, 'Cart/detail.html', {'cart':cart, 'store_id':store_id,
                                                'coupon_form':coupon_form})
