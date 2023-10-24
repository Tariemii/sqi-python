"""
consider your self a instructor, that has 7 students.
you want your students to do a cbt exam, 
when they want to write the exam, they should input their name and address 
when they are done. print {ola} scored {20}. with the name being the key and score being the value 
the person with the highest score from dugbe is ola with {score} marks
"""
scores = []
studentinfo = {}

for i in range(3):
    username = input("Enter your name:")
    score = 0
    nt = 0
    questions = ["Where is Sqi located?", "Sqi is what type of school?",
             "Who is the president of Nigeria?"]
    options = ["a. Heritage mall\nb. Central Bank\nc. Cocoa House", 
           "a.Coding School\nb.Business school\nc. Fashion school", "a. Tinubu\n b. Obi\n c. Atiku"]
    answers = ["a", "a", "a", "c"]

    for question in questions:
     print(question)
     print(options[nt])
     student_answer = input("Please enter your answer:")
     ans = answers[nt]
     if student_answer == ans:
            print("correct answer") 
            score += 10
     else:
            print("Wrong answer")
            score -= 5
     nt += 1
    print(score)
   
    scores.append(score)
    studentinfo[username] = score
    print(studentinfo)
    print(f"{username}'s score is {score}")
    
    # keymax = max(zip(studentinfo.values(), studentinfo.keys()))
    keymax = max(studentinfo, key=studentinfo.get)
print('The student with the highest score is:' + keymax)