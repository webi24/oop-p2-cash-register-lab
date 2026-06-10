class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if not isinstance(value, int) or isinstance(value, bool):
            print("Not valid discount")
            if not hasattr(self, "_discount"):
                self._discount = 0
            return
        if value < 0 or value > 100:
            print("Not valid discount")
            if not hasattr(self, "_discount"):
                self._discount = 0
            return
        self._discount = value

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.total = round(self.total, 2)
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return
        savings = self.total * (self.discount / 100)
        self.total = round(self.total - savings, 2)
        return self.total

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There are no transactions to void.")
            return
        last = self.previous_transactions.pop()
        subtotal = last["price"] * last["quantity"]
        for _ in range(last["quantity"]):
            if last["item"] in self.items:
                idx = len(self.items) - 1 - self.items[::-1].index(last["item"])
                self.items.pop(idx)
        self.total = round(self.total - subtotal, 2)
