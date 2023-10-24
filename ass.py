"""
Write a program that will ask user his or her fullname, age, address, and course
Print this statement in the following order:
My name is ----, i am age years old,
"""

print("Please put in the information required")
firstname = input("First Name:")
lastname = input("Last Name:")
address = input("Address:")
age = int(input("Age:"))
score = float(input("Score:"))
print(f"My name is {firstname} {lastname}, I am {age} years old, I am from {address} and my score is {score}")