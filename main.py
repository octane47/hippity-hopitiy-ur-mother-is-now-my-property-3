import string

alphabets = string.ascii_lowercase + string.ascii_lowercase

sentence = list (input("enter your text : \n").lower())

what_to_do = input("enter encrypt to encrypt, decrypt to cecrypt, exit to exit the program \n'").lower()

shift_number = int(input('enter you sift number from 1 to 25: \n'))

end_program = False


while not end_program:
  #search through enter text
  if what_to_do == 'encrypt':
      for i in range(len(sentence)):
          #get the position of each character within the sentence
          if sentence[i] =='':
              sentence[i] = ''
          else:
              new_letter = alphabets.index(sentence[i]) + shift_number
              sentence[i] = alphabets[new_letter]
      #convert the list back to a string
      print('',join(map(str,sentence)))
      end_program = True
  elif what_to_do == 'decrypt':
      for i in range(len(sentence)):
          #get the position of each character within the sentence
          if sentence[i] =='':
              sentence[i] = ''
          else:
              new_letter = alphabets.index(sentence[i]) + shift_number
              sentence[i] = alphabets[new_letter]
      #convert the list back to a string
      print('',join(map(str,sentence)))
      end_program = True