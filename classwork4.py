import random
import mysql.connector 
conn = mysql.connector.connect(host = "127.0.0.1", user = 'root', password = "busola4ella.", database = "school")
cursor = conn.cursor()

class cbt:
    def __init__(self):
        print("You're welcome")
        self.home()
    
    def home(self):
        self.login2 = input('What would you like to do\n1.Login\n2.Register\n3.LEAVE\n')
        if self.login2 == '1':
            self.login()
        elif self.login2 == '2':
            self.register()
        else:
            print('BYEEEEEE!!!')
            
    def register(self):
        self.register2 =  input("Enter your full name: ")
        self.username= input("Enter your username: ")
        self.password= input("Enter your password: ")
        self.querry = 'INSERT INTO cbt( fname,username, pass_word, score) VALUES( %s, %s, %s, %s)'
        self.val = ( self.register2, self.username, self.password)
        cursor.execute(self.querry, self.val)
        conn.commit()
        print('Registration successful')
        self.home()
            
    def login(self):
        self.user = input('Enter your username: ')
        self.passw = input('Enter your password: ')
        self.querry = 'SELECT * FROM cbt WHERE username = %s'
        self.val = (self.user,)
        cursor.execute(self.querry,self.val)
        self.result = cursor.fetchone()
        self.confirm()
    
    def confirm(self):
        if self.user == self.result[2] and self.passw == self.result[3]:
            print('Login successful')
            self.cbtt()
        else:
            self.login()
            # self.cbt1 = input('What will you like to do?\n1.Write cbt exam\n2.Leave\n')
            # if self.cbt1 == '1':
            #     self.cbtt()
            # else:
            #     self.home()
            
    
    def cbtt(self):
        scores, nt = 0, 0
        questions = ["Where is Sqi located?", "Sqi is what type of school?",
             "Who is the president of Nigeria?", "Which country won the last world cup?"]
        options = ["a. Heritage mall\nb. Central Bank\nc. Cocoa House", 
                "a.Coding School\nb.Business school\nc. Fashion school", "a. Tinubu\n b. Obi\n c. Atiku",
                "a. Nigeria\n b.France\nc. Argentina"]
        answers = ["a", "a", "a", "c"]
        
        for question in questions:
         print(question)
         print(options[nt])
         student_answer = input("Please enter your answer:")
         # ans = answers[nt]
         if student_answer == answers[nt]:
                print("correct answer") 
                scores += 10
         else:
                print("Wrong answer")
                scores -= 5
         nt += 1
         print(scores)
        print(f"Your total score is {scores}")
        querry = 'update cbt set score = %s where username = %s'
        score = scores
        val = (score, self.user)
        cursor.execute(querry, val)
        conn.commit()
        self.home()

cbt()       
        