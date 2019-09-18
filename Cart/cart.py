from decimal import Decimal
from django.conf import settings
from Food.models import Food
from Coupon.models import Coupon

class Cart(object):

    def __init__(self, request):

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

        self.coupon_id = self.session.get('coupon_id')
        self.store_id = self.session.get('store_id')

    def add(self, food, store_id, quantity=1, update_quantity=False):
        food_id = str(food.id)
        if food_id not in self.cart:
            self.cart[food_id] ={'quantity':0, 'price':str(food.price),'store_id':int(store_id)}
        if update_quantity:
            self.cart[food_id]['quantity'] = quantity
        else:
            self.cart[food_id]['quantity'] += quantity

        self.save()


    def save(self):
        self.session.modified = True

    def remove(self,food):
        food_id = str(food.id)
        if food_id in self.cart:
            del self.cart[food_id]
        self.save()

    def __iter__(self):

        food_ids = self.cart.keys()

        foods = Food.objects.filter(id__in=food_ids)
        cart = self.cart.copy()
        for food in foods:
            cart[str(food.id)]['food'] = food
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(item['quantity'] * item['price'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def check_empty(self):
        if self.cart.values() is None:
            self.cart['coupon_id'] = None
            return True
        return False


    def get_store_id(self):
        store_id = 0
        for item in self.cart.values():
            store_id = item['store_id']
            break
        return store_id

    @property
    def coupon(self):
        if self.coupon_id:
            return Coupon.objects.get(id=self.coupon_id)
        return None

    def get_discount(self):
        if self.coupon:
            return (self.coupon.discount / Decimal('100')) * self.get_total_price()
        return Decimal('0')

    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()
