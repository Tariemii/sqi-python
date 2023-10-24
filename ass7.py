# username = ['ella', 'tom']
# password = ['1234', '5678']
"""
Write a program that will ask user for their username and password. 
Note: if the username and password is in the array of username and password,
it should login, else invalid login details. Futhermore, after login, your program should
set cbt questions and ask for answer, if the user answer is the same as your answer,
 score the user and add 10 marks, else -5marks"""
 
score, nt = 0, 0
questions = ["Where is Sqi located?", "Sqi is what type of school?",
             "Who is the president of Nigeria?", "Which country won the last world cup?"]
options = ["a. Heritage mall\nb. Central Bank\nc. Cocoa House", 
           "a.Coding School\nb.Business school\nc. Fashion school", "a. Tinubu\n b. Obi\n c. Atiku",
           "a. Nigeria\n b.France\nc. Argentina"]
answers = ["a", "a", "a", "c"]


uname = ['ola', 'seun']
pwd = ['1234', '5678']
username = input('Enter your username:')
passwd = input('Enter your password:')
x = list(zip(uname,pwd))
if (username, passwd) in x:
    print('Login successful')
    for question in questions:
        print(question)
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
   
else:
    print('Login failed')
    
    

# if username in uname and passwd == pwd[uname.index(username)]:
#     print ('Login succesful')
# else:
#     print('Login failed')
    
# ind = uname.index(username)
# if username in uname and passwd == pwd[ind]:
#        print ('Login succesful')
# else:
#     print('Login failed')
    