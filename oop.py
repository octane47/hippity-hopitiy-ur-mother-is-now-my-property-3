import string

plain_text = "hello world"
shift = 3


e_alphabet = string.ascii_lowercase
shifted = e_alphabet[shift:] + e_alphabet[:shift]
table = str.maketrans(e_alphabet, shifted)

encrypted = plain_text.translate(table)

print(encrypted)