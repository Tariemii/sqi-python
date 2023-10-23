import mysql.connector as std
conn = std.connect(host = "127.0.0.1", user = "root", password = "", database = "voting")
cursor = conn.cursor()
import random, time

class voting:
    def __init__(self):
        print("Welcome to SQI's voting page!!!")
        self.stdinfo = []
        self.dept = ["Data science", "Data Analysis", "Web Development", "JavaScript", "Graphic Design and Multimedia", "Cyber Security", "UI/UX"]
        self.deptnum = ["1", "2", "3", "4", "5", "6", "7"]
        self.depart = ["DS", "DA", "WB", "JS", "GP", "CS", "UX"]
        self.main_dept = tuple(zip(self.dept, self.deptnum, self.depart))
        self.candidate = {
            "president" : ["Tammy", "Jomiloju", "Billiaminu"],
            "vice_president" : ["Sewa", "Ini", "Bode"],
            "gen_sec" : ["Michael", "Joba", "Nathaniel"]
        }
        self.start()
        
    #This is the welcome page     
    def start(self):
        self.home = input("What will you like to do?\n1.Register\n2.Login\n3.View election result\n4.Leave\n>>>")
        if self.home == "1":
            self.register()
        elif self.home == '2':
           admin = input("1.Login as an admin\n2.Login as a student\n>>> ")
           if admin == "1":
                self.login2()
           elif admin == "2":
                self.login()
        elif self.home == '3':
            self.view()
        else:
            print("Goodbyee")
            
    #This is the code for students to register    
    def register(self):
        print('These are the departments available for voting:')
        self.dep_num = 1
        for i in self.dept:
            print(f"{self.dep_num}. {i}\n")
            self.dep_num += 1
            
        self.dept1 = input("Pick your department: ")
        while self.dept1 not in self.deptnum:
            print(f"Department not avaliable\n")
            self.dept1 = input("Pick your department: ")
        self.deptt = self.main_dept[self.deptnum.index(self.dept1)][2]
        self.deptname = self.main_dept[self.deptnum.index(self.dept1)][0]
        self.cardno = str(random.randrange(100, 999))
        self.card = self.deptt + self.cardno
        self.stdinfo.append(self.card)
        
        self.info = ["Fullname", "Password", "Level"]
        for i in self.info:
            self.userinfo = input(f"Enter Your {i}: ")
            self.stdinfo.append(self.userinfo)
            
        self.stdinfo.append(self.deptname)
        self.querry = "insert into student_info (card_number, fullname, pass_word, lvl, dept) values(%s, %s, %s, %s, %s)"
        self.val = (self.stdinfo)
        print(self.val)
        cursor.execute(self.querry, self.val, )
        conn.commit()
        print('Processing...')
        time.sleep(1)
        print('Registration successful')
        print(f'Your card number is {self.stdinfo[0]}')
        log_op = input("\nDo you want to log into your account Y/N: ").upper().strip()
        if log_op == "Y":
            self.login()
        elif log_op == "N":
            print(f"Goodbye, {self.stdinfo[1]}")

        # self.start()
    
    #This is the code for students to login
    def login(self):
        self.card_no = input("Enter your card number: ").strip()
        self.password = input("Enter your password: ").strip()
        self.cquerry = "SELECT * FROM student_info WHERE card_number = %s "
        self.cval = (self.card_no,)
        cursor.execute(self.cquerry, self.cval)
        self.result = cursor.fetchone()
        if self.card_no:
            print("PROCESSING...")
            if self.card_no == self.result[1] and self.password == self.result[3]:
                time.sleep(1)
                print("LOGIN SUCCESSFUL")
                time.sleep(1)
                self.platform()
            else:
                time.sleep(1)
                print("INVALID LOGIN DETAILS, TRY AGAIN")
                time.sleep(1)
                self.login()
   
    #This is the code for admin to login
    def login2(self):
        self.userad = input("Enter your username: ")
        self.passad = input("Enter your password: ")
        self.adquerry = "select * from staff_admin where username = %s"
        self.adval = (self.userad,)
        cursor.execute(self.adquerry,self.adval)
        self.adresult = cursor.fetchone()
        if self.userad:
            if self.userad == self.adresult[1] and self.passad == self.adresult[2]:
                time.sleep(1)
                print("LOGIN SUCCESSFUL")
                time.sleep(1)
                self.ad_welcome()
            else:
                time.sleep(1)
                print("INVALID LOGINN DETAILS, TRY AGAIN")
                time.sleep(1)
                self.login2()
    
    def ad_welcome(self):
        self.end = input("1.view results\n2.list who voted for a candidate\n3.list who voted for a candidate in a particular dept\n4.change password\n5.Leave\n>>>")
        if self.end == "1":
            self.view()
        elif self.end == "2":
            self.can()
        elif self.end == "3":
            self.can_dept()
        elif self.end == "4":
            self.changeP()
        elif self.end == "5":
            self.start()
        else:
            print("Goodbye")
    
    #This code allows the admin to check the students who voted in a particular category       
    def can(self):
        self.canResult = input("Enter the category you want to view: (President, Vice_president and Gen_secretary)\n>>> ").lower()
        print(f"candidates in this category are {self.candidate[self.canResult]}")
        self.canResult1 = input("Enter the candidate you want to check for: ")
        query = f"select fullname from student_info where {self.canResult} = {'%s'}"
        val = (self.canResult1,)
        cursor.execute(query,val)
        names = cursor.fetchall()
        for i in names:
            print(i[0])
            time.sleep(1)
        self.ad_welcome()
     
    #This code allows the admin to check the students who voted in a parrticular department  
    def can_dept(self):
        print(f"The avaliable departmants are {self.dept}")
        self.dept_inpResult = input("Enter the department to check result: ")
        self.canResult = input("Enter the category you want to view: (President, Vice_president and Gen_secretary)\n:>>> ").lower()
        print(f"candidates in this category are {self.candidate[self.canResult]}")
        self.canResult1 = input("Enter the candidate you want to check for: ")
        query = f"select fullname from student_info where dept = {'%s'} and {self.canResult} = {'%s'}"
        val = (self.dept_inpResult, self.canResult1)
        cursor.execute(query,val)
        names = cursor.fetchall()
        for i in names:
            print(i[0])
            time.sleep(1)
        self.ad_welcome()
    
    #This code allows the admin to change their passwords    
    def changeP(self): 
        query = "select username from staff_admin"
        cursor.execute(query)
        user = cursor.fetchall()
        ad_user = input("Enter your username: ")
        if (ad_user,) in user:
            ad_pass = input("Enter your old password: ")
            ad_pass2 = input("Enter your new password: ")
            ad_Npass = input("confirm your password: ")
            while ad_pass2 != ad_Npass:
                print("PASSWORDS DO NOT MATCH") 
                ad_Npass = input("confirm your password: ")
        else:
            print("username not in database")
            print(user)
            time.sleep(1)
            self.changeP()
        Pquery = "UPDATE staff_admin SET pass_word = %s WHERE username = %s"
        Pval = (ad_pass2, ad_user)
        cursor.execute(Pquery, Pval)
        conn.commit()
        self.ad_welcome()
        
    #This is the main code for voting           
    def platform(self):
        cursor.execute(self.cquerry, self.cval)
        self.result = cursor.fetchone()
        print(f"\nWelcome {self.result[2]}, to SQI'S Voting Platform\nThe following are the posts to vote for: (President, Vice_President and Gen_Sec)\nEnter 0 to Exit ")
        self.vote_candidate = input("Pick a post: ").lower()
        if self.vote_candidate in self.candidate.keys():
            print("PROCESSING...")
            time.sleep(1)
            if self.vote_candidate == "president":
                count = 6
            elif self.vote_candidate == "vice_president":
                count = 7
            elif self.vote_candidate == "gen_sec":
                count = 8
                
            if self.result[count] == None:  
                a=1
                for i in (self.candidate[self.vote_candidate]):
                    print(f"{a}. {i}")
                    a += 1
                self.choose = input("Enter the name of the candidate you want to vote for: ").capitalize()
                if self.choose in self.candidate[self.vote_candidate]:
                    print('you have voted',self.choose,'for ',self.vote_candidate )
                    self.query = f"update student_info set {self.vote_candidate} = {'%s'} where card_number = {'%s'} "
                    self.val = (self.choose, self.card_no)
                    cursor.execute(self.query, self.val)
                    conn.commit()
                    time.sleep(1)
                    self.again = input("Would you like to vote for another category?\n1.Yes\n2.No\n>>>")
                    if self.again == "1":
                        self.platform()
                    elif self.again == "2":
                        print("Thank you for voting")
                        self.start()
                else:
                    print("Candidate not found")
                    self.platform()
            else:
                print("You have voted in this category")  
                self.platform()
        elif self.vote_candidate == "0":
            print(f"Goodbye. {self.result[2]}") 
            self.start() 
        else:
            print("Category not found")
            self.platform()  
    
    #This is the code for viewing results
    def view(self):
        self.winner = {}
        self.usit = input("1.General result\n2.Department result\n3.Exit\n>>>")
        if self.usit == "1":
            self.inp = input("Enter the category you want to view: (President, Vice_president and Gen_sec)\n:>>> ").lower()
            if self.inp in self.candidate.keys():
                for name in self.candidate[self.inp]:
                    print(f"{name} had {self.cc(name)[0]} votes")
                    self.winner.update({name:self.cc(name)[0]})
                self.viewtie()
            else:
                print("category not found")
                time.sleep(1)
                self.view()
        elif self.usit == "2":
            print(f"The departments are {self.dept}")
            self.dept_inp = input("Enter the department to check result: ")
            if self.dept_inp in self.dept:
                self.inp = input("Enter the category you want to view: (President, Vice_president and Gen_sec)\n>>>").lower()
                if self.inp in self.candidate.keys():
                    for name in self.candidate[self.inp]:
                        print(f"{name} had {self.cc2(self.dept_inp,name)[0]} votes")
                        self.winner.update({name:self.cc2(self.dept_inp,name)[0]})
                    self.viewtie()
            else:
                print("category not found")
                time.sleep(1)
                self.view()
    
    def viewtie(self):
        win_arr = []
        for key, val in self.winner.items():
            if val == max(self.winner.values()):
                win_arr.append(key)
        
        if len(win_arr) > 1:
            print("There is a tie between these candidates: ")
            for i in win_arr:
                print(i)
        else:
            print(f"{max(self.winner, key=self.winner.get)} is the winner")
        self.winner = {}
        decide = input("1.View again\n2.Leave\n>>> ")
        if decide == "1":
            self.view()
        else:
            self.start()
    
    def cc(self, name):
        self.query= f"select count({self.inp}) from student_info where {self.inp} = {'%s'}"
        self.val = (name,)
        cursor.execute(self.query, self.val)
        res = cursor.fetchone()
        return res
        
    def cc2(self, dept, name):
        self.query= f"select count({self.inp}) from student_info where dept = {'%s'} and {self.inp} = {'%s'}"
        self.val = (dept, name)
        cursor.execute(self.query, self.val)
        res = cursor.fetchone()
        return res   
         
voting()