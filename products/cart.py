class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity=1):
        if product.id not in self.items:
            self.items[product.id] = {'product': product, 'quantity': quantity}
        else:
            self.items[product.id]['quantity'] += quantity

    def remove_item(self, product_id):
        if product_id in self.items:
            del self.items[product_id]

    def get_total_price(self):
        total_price = 0
        for item in self.items.values():
            total_price += item['product'].price * item['quantity']
        return total_price

    def clear_cart(self):
        self.items = {}
