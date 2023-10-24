"""Design a simple calculator where the user can perform any operation the user wants"""
val1 = float(input("Enter the first value:"))
operation = input("""
      Enter 1 to perform addition
      Enter 2 to perform subtraction
      Enter 3 to perform multiplication
      Enter 4 to perform Division""")
val2 = float(input("Enter the second value:"))

if operation == "1":
    print(val1 + val2)
elif operation == "2":
    print(val1 - val2)
elif operation == "3":
    print(val1 * val2)
elif operation == "4":
    print(val1/val2)
else:
    print("Invalid operation")
    
    
   