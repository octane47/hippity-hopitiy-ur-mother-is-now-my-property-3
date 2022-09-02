import string
#hey just change the e to something to that can mean encyption and paste then change it to something that can mean decyption and then woah wow you did it 
print(" this is your friendly encryption and decryption program")
print()
answer = input("what would you like to do?, encrypt or decrypt?")
print()


if answer = encrypt:
  en_reply = input(" enter word or phrase you with to encrypt")
  shift = 3
  en_alphabet = string.ascii_lowercase
  shifted = en_alphabet[shift:] + en_alphabet[:shift]
  table = str.maketrans(en_alphabet, shifted)
  
  encrypted = en_reply.translate(table)
  print()
  print()
  print(" )



shift = -3


de_alphabet = string.ascii_lowercase
shifted = de_alphabet[shift:] + de_alphabet[:shift]
table = str.maketrans(de_alphabet, shifted)

encrypted = plain_text.translate(table)

print(encrypted)

