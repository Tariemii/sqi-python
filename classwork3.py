# import random
# fname = []
# usr_age = []
# pnumber = []
# usr_address = []
# usr_account = []

# print('Welcome to the bank portal')
# print('Please enter the details below')

# x = input("input 'd' to quit" )
# while x != 'd':
    
#   fullname = input('Enter your fullname:')
#   age = int(input('Enter your age:'))
#   while age < 18:
#       print('You are too young')
#       age = int(input('Enter your age:')) 
      
#   phone_number = input('Enter your phone number:')
#   while len(phone_number) != 11:
#     print("Phone number must be 11 digits")
#     phone_number = input('Enter phone number:')
    
#   address = input('Enter your address:')
#   account = phone_number[1:]
#   bvn = random.randint(123456789011, 9012098765431)
  
#   fname.append(fullname)
#   usr_age.append(age)
#   pnumber.append(phone_number)
#   usr_address.append(address)
#   print(f"Your account number is {account}")
#   print(f"Your bank verification number is {bvn}")
#   print(fname, usr_age, pnumber, usr_address, account, bvn)
  
import random

combo = {}
entry = input("Enter your number to register or enter stop to quit")
while entry != 'stop':
    info = ["fullname", "age", "phone", "address"]
    general = []
    for i in info:
      information = input(f'Enter your {i}:')
      while i == 'phone' and len(information) != 11:
            print('Phone number should not be more or less than 11')
            information = input(f'Enter your {i}:')
      general.append(information)
    account = general[2][1:]
    general.append(account)
    bvn = random.randrange(1234567891010, 9876543210101)
    general.append(bvn)
    combo.update({entry:general})
    entry = input("Enter your number to register or enter stop to quit")
else:
    print('YAAAAY')
    print(combo)
  