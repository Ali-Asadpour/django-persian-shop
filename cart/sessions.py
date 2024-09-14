import cart


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def save(self):
        self.session.modified = True


    def unique_id_generator(self, id, color):
        return f'{id}_{color}'


    def add_to_cart(self,product, id, color, quantity):
        unique_id = self.unique_id_generator(id, color)
        if unique_id not in self.cart:
            self.cart[unique_id] = {'id': id, 'color': color, 'quantity': quantity,'product': product}
        else:
            self.cart[unique_id]['quantity'] += quantity




