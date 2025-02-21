from store.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.setdefault('session_key', {})

    def add(self, product):
        self.cart.setdefault(str(product.id), {'price': str(product.price)})
        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_prdt(self):
        return Product.objects.filter(id__in=self.cart.keys())
