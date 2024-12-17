
'password generator'

from random import randint
password = []

amount = int(input("how long should the password be: "))

for i in range(0,amount):
     digit = randint(0,9)
     password.append(digit)
     #convert password to string
     str_password= "".join(str(i) for i in password)
     
     
     
print(str_password)
