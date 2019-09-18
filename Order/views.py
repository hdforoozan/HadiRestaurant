from django.shortcuts import render
from Cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form  = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            if cart.store_id:
                order.store_id = cart.store_id
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,food=item['food'],
                                        price=item['price'],quantity=item['quantity'])
            cart.clear()
            return render(request, 'Order/create_done.html', {'order':order})
    else:
        form = OrderCreateForm()

    return render(request, 'Order/create.html', {'cart':cart, 'form':form})
