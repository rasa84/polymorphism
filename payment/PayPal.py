class PayPal:
    def __init__(self, balance=0):
        self.balance = balance

    def process_payment(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Mokėjimas vykdomas. Suma: {amount} EUR")
        else:
            print("Nepakankamas likutis")

    def __add__(self, other):
        return PayPal(self.balance + other)

    def __sub__(self, other):
        return PayPal(self.balance - other)

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __str__(self):
        return f"PayPal balansas = {self.balance} EUR"
