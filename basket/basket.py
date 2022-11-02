from decimal import Decimal
from store.models import Product
from django.conf import settings


class Basket():
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if settings.BASKET_SESSION_ID not in request.session:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    def add(self, product, qty):
        product_id = product.id

        if product_id not in self.basket:
            self.basket[product_id] = {"price": str(product.price), "qty": int(qty)}
        
        self.save()

    def __iter__(self):
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]["product"] = product
        
        for item in basket.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["qty"]
            yield item

    def __len__(self):
        return sum(item["qty"] for item in self.basket.values())

    def get_subtotal_price(self):
        return sum(Decimal(item["price"]) * item["qty"] for item in self.basket.values())

    def get_total_price(self):
        subtotal = sum(Decimal(item["price"]) * item["qty"] for item in self.basket.values())

        if subtotal == 0:
            shipping = Decimal(0.00)
        else:
            shipping = Decimal(11.50)

        total = subtotal + Decimal(shipping)
        return total 
    
    def delete(self, product):
        product_id = str(product)

        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def update(self, product, qty):
        product_id = str(product)

        if product_id in self.basket:
            self.basket[product_id]["qty"] = qty
        
        self.save()

    
    def save(self):
        self.session.modified = True

    
    def clear(self):
        del self.session[settings.BASKET_SESSION_ID]
        self.save()
