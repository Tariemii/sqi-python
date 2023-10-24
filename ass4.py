"""
write a program that will ask a food seller the food and protein she has, if her food is rice and her protein is 
egg, tell the seller that you will buy rice and egg, else you will not buy anything 
"""
food1 = input("Which food do you have")
protein = input("what protein do you have")
if food1 == "rice" and protein == "meat":
     print("I will buy rice ang egg")
else:
     print("I am not buying")