import re


class SmsSender:
    max_symbols_num = 100

    def send_message(self, destination, message):
        if not re.match(r"^\+370\d{3}\d{5}$", destination):
            print(f"Neteisingas telefono numeris: {destination}")
            return
        if len(message) > SmsSender.max_symbols_num:
            print(f"Žinutė viršija maksimalų simbolių skaičiu: {SmsSender.max_symbols_num}")
            return
        print(f"Siunčiama SMS \"{message}\" į {destination}")
