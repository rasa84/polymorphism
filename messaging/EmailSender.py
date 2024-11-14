import re


class EmailSender:
    def send_message(self, destination, message):
        if not  re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', destination):
            print(f"Neteisingas el. pašto adresas: {destination}")
            return
        print(f"Siunčiama žinutė \"{message}\" į {destination}")
