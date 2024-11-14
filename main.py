from cooking.Recipe import Recipe
from messaging.EmailSender import EmailSender
from messaging.SmsSender import SmsSender
from payment.BankTransfer import BankTransfer
from payment.CreditCard import CreditCard
from payment.PayPal import PayPal
from shop.Product import Product


def make_payment(payment_method, amount):
    payment_method.process_payment(amount)


credit_card = CreditCard(200)
paypal = PayPal(450)
bank_transfer = BankTransfer(780)

make_payment(credit_card, 100)
make_payment(paypal, 200)
make_payment(bank_transfer, 300)

print(credit_card)
print(paypal)
print(bank_transfer)

print(credit_card == paypal)
print(credit_card < bank_transfer)
print(credit_card > bank_transfer)
print(paypal < credit_card)

credit_card = credit_card + 100
print(credit_card)

bank_transfer = bank_transfer - 100
print(bank_transfer)

print("------------------------------------------------------------------------------------------------------------")
email_sender = EmailSender()
sms_sender = SmsSender()

email_messages = [
    {"destination": "test@test.com", "message": "Labas, kaip gyveni?"},
    {"destination": "wrong_email.com", "message": "Neteisingas el. pašto adresas"},
]
sms_messages = [
    {"destination": "+37067589562", "message": "Siunčiu tau SMS, siunčiu tau SOS"},
    {"destination": "12456887", "message": "Neteisingas telefono numeris."},
    {"destination": "+37067588885", "message": "Per ilga žinutė" * 10},
]


def send_message(sender, messages):
    for msg in messages:
        sender.send_message(msg["destination"], msg["message"])


send_message(email_sender, email_messages)
send_message(sms_sender, sms_messages)

print("------------------------------------------------------------------------------------------------------------")

recipe = Recipe("Pyragas", {"miltai": 200, "pienas": 300, "kiaušiniai": 2, "obuoliai": 8, "cukrus": 200}, 4)
print(recipe)
larger_recipe = recipe * 2
print(larger_recipe)
smaller_recipe = recipe / 2
print(smaller_recipe)

print("------------------------------------------------------------------------------------------------------------")

product1 = Product("Saldainiai", 4.5, 8.20)
product2 = Product("Sausainiai", 8.2, 2.80)

print(product1)
print(product2)

print(product1 == product2)
print(product1 != product2)
print(product1 < product2)
print(product1 <= product2)
print(product1 > product2)
print(product1 >= product2)
