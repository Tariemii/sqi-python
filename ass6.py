"""
write a python program that will set questions, set options[set], set answers[if,else], ask users for answers[print input]
mark the answers[if, else], if the user gets a question, your program sould be able to score the user 10marks[ like a calc]
and for every question missed the program should minus[ like a calc]
"""
import time
score = 0
nt = 0

questions = ["Where is Sqi located?", "Sqi is what type of school?",
             "Who is the president of Nigeria?", "Which country won the last world cup?"]
options = ["a. Heritage mall\nb. Central Bank\nc. Cocoa House", 
           "a.Coding School\nb.Business school\nc. Fashion school", "a. Tinubu\n b. Obi\n c. Atiku",
           "a. Nigeria\n b.France\nc. Argentina"]
answers = ["a", "a", "a", "c"]

for question in questions:
    print(question)
    time.sleep(2)
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
    time.sleep(2)
print(f"Your total score is {score}")
    