"""using your previous code, include password to it
create a general program that user will be able to login with the matric number and the password
the should be able to perform any of these operations
cbt
set operations
calculator
food seller assignment
when the user is done code must ask if user wants to perform another operation"""

import random
password = []
matricnum = []
std_info = {}
  


et= {}
mykey = input('Enter start to register or stop to quit:')
while mykey != 'stop':
    stdinfo = ['Fullname', 'Middlename', 'Lastname', 'Age', 'Gender', 'Phone number', 'Address']
    myvalue = []
    for i in stdinfo:
        information = input(f"Please enter your {i}:")
        while i == 'Phone number' and len(information) != 11:
            print('your phone number must not be more or less than 11 digits')
            information = input(f"Please enter your {i}:")
        myvalue.append(information)
    regnumber = myvalue[5][4:]
    myvalue.append(regnumber)
    matricno = random.randrange(1234, 6789)
    endchar = 'SQI'
    matricnumber = str(matricno)+endchar
    matricnum.append(matricnumber)
    myvalue.append(matricnumber)
    pwd = input('enter your password:')
    password.append(pwd)
    myvalue.append(password)
    et.update({mykey:myvalue}) #et[mykey] = myvalue
    mykey = input('Enter start to register or stop to quit')
else:
    print('Bye')
print( "All students information:\n", et)
login = list(zip(matricnum, password))
print(f'your matric no and password is {login}')

def cbt():
    score, nt = 0, 0
    questions = ["Where is Sqi located?", "Sqi is what type of school?",
                "Who is the president of Nigeria?", "Which country won the last world cup?"]
    options = ["a. Heritage mall\nb. Central Bank\nc. Cocoa House", 
            "a.Coding School\nb.Business school\nc. Fashion school", "a. Tinubu\n b. Obi\n c. Atiku",
            "a. Nigeria\n b.France\nc. Argentina"]
    answers = ["a", "a", "a", "c"]

    for question in questions:
        print(question)
        # time.sleep(2)
        print(options[nt])
        student_answer = input("Please enter your answer:")
        # ans = answers[nt]
        if student_answer == answers[nt]:
            print("correct answer") 
            score += 10
        else:
            print("Wrong answer")
            score -= 5
        nt += 1
        print(score)
    
    print(f"Your total score is {score}")
def  sets():
    s1, s2, s3 = [], [],[]
    for i in range(4):
        se1 = input('Enter the first set:')
        se2 = input('Enter your second set:')
        se3 = input('Enter the third set:')
        s1.append(se1)
        s2.append(se2)
        s3.append(se3)
    set1, set2, set3 = set(s1), set(s2), set(s3)
    operation = input("""Choose operation to perform
                    Enter 1 for union
                    Enter 2 for intersection
                    Enter 3 for symmetric difference:
                    """)
    if operation == "1":
        set4 =set1.union(set2).union(set3)
        print(set4)
    elif operation == '2':
        set4 = set1.intersection(set2).intersection(set3)
        print(set4)
    elif operation == '3':
        set4 = set1.symmetric_difference(set2).symmetric_difference(set3)
        print(set4)
def calc():
    val1 = float(input("Enter the first value:"))
    operation = input("""
        Enter 1 to perform addition
        Enter 2 to perrform subtraction
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
def  food():
   food1 = input("Which food do you have")
   protein = input("what protein do you have")
   if food1 == "rice" and protein == "meat":
        print("I will buy rice ang egg")
   else:
        print("I am not buying")  

log = input('Do you want to login in? yes/no:')
if log == 'yes':
    username = input('Enter your matric number:')
    pass_word = input('Enter your password:')
    while (username, pass_word) in login:
     operation = input("""what operation will you like to perform?or stop to quit\n 1.cbt\n2.sets\n3.calculator.\n4.food\n Enter:""")
     while operation != 'stop':
        if operation == '1':
            cbt()
            break
        elif operation == '2':
            sets()
            break
        elif operation == '3':
            calc()
            break
        elif operation == '4':
            food()
            break
     else:
         break
   
        
     
    
    
    
    
