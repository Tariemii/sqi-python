"""
collect info name age and address from 5 student, 
write a program that will collect it and print it all at the end of the program
"""
name = []
address = []
age = []

for i in range(5):
  user = input('Enter your name:')
  user_age = int(input('Enter your age:'))
  user_address = input('Enter your address:')
  name.append(user)
  age.append(user_age)
  address.append(user_address)
  print(name, age, address)