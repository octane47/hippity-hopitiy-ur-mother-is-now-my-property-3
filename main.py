import string
#hey just change the e to something to that can mean encyption and paste then change it to something that can mean decyption and then woah wow you did it 
def en_alphabet_de_alphabet(question):
    vaild = False
    while not vaild:
        response = input(question).lower()

        if response == "en_alphabet" or response == "encrypt":
            response = "yes"
            return response

        if response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please answer yes / no")

plain_text = "hello world"
shift = 3


en_alphabet = string.ascii_lowercase
shifted = en_alphabet[shift:] + en_alphabet[:shift]
table = str.maketrans(en_alphabet, shifted)

encrypted = plain_text.translate(table)

print(encrypted)
import string

plain_text = "hello world"
shift = -3


de_alphabet = string.ascii_lowercase
shifted = de_alphabet[shift:] + de_alphabet[:shift]
table = str.maketrans(de_alphabet, shifted)

encrypted = plain_text.translate(table)

print(encrypted)

