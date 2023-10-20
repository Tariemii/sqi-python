import random
import mysql.connector 
conn = mysql.connector.connect(host = "127.0.0.1", user = 'root', password = "busola4ella.", database = "BANK")
cursor = conn.cursor()

class me:
    def __init__(self):
        print('Welcome!!!')
        self.start()
        
    def start(self):
        self.operation = input('What will you like to do today?\n1.Login\n2.Sign up for a new account\n3.Deposit\n4.Exit\n>>>')
        if self.operation == '1':
            self.login()
        elif self.operation == '2':
            self.register()
        elif self.operation == '3':
            self.deposit()
        else:
            print('Thank you for using our services')
            
    def register(self):
        self.user_info = []
        self.information = ['first name', 'last name', 'Age', 'Gender', 'Address', 'Phonenumber','Password']
        for info in self.information:
            decision = input(f'Enter your {info}:')
            while info == 'Phonenumber' and len(decision) != 11:
                print('Phone number must be 11 digits')
                decision = input(f'Enter your {info}:')
            self.user_info.append(decision)
            while info == 'Age' and int(decision) < 18:
                print('You are not eligible to create this account!!!')
        self.accountnumber = self.user_info[5][1:]
        self.user_info.append(self.accountnumber)
        self.bvn = random.randrange(123456789, 987654321)
        self.user_info.append(self.bvn)
        self.accountbalance = 0
        self.user_info.append(self.accountbalance) 
        print(self.user_info)
        self.open()
        
    def open(self):
        self.which = input('Which bank would you like to open\n>>>').lower()
        if self.which == 'gtbank':
            self.querry = 'INSERT INTO gtbank (fname, lname, Age, Gender, Address, phonenumber, pass_word, accountnumber, BVN, accountbalance ) VALUES(%s,%s, %s, %s, %s, %s, %s, %s,%s,%s)'
            self.next()
        elif self.which == 'stanbic':
            self.querry = 'INSERT INTO stanbic (fname, lname, Age, Gender, Address, phonenumber, pass_word, accountnumber, BVN, accountbalance ) VALUES(%s,%s, %s, %s, %s, %s, %s, %s,%s,%s)'
            self.next()
        elif self.which == 'zenith':
            self.querry = 'INSERT INTO gtbank (fname, lname, Age, Gender, Address, phonenumber, pass_word, accountnumber, BVN, accountbalance ) VALUES(%s,%s, %s, %s, %s, %s, %s, %s,%s,%s)'
            self.next()
    
    def next(self):
            self.val = tuple(self.user_info)
            cursor.execute(self.querry, self.val)
            conn.commit()
            print(f'You have successfully registered and your account number is {self.accountnumber} and your password is {self.user_info[6]}')
            self.log = input('1.Would you like to login to your account\n2.Would you like to deposit into your account before you login\n3.Leave\n')
            if self.log == '1':
                self.login()
            elif self.log == '2':
                self.deposit()
            else:
                print('Thank you for using our services')
                
    def login(self):
        self.user = input("Enter your account number ").strip()
        self.passw = input("Enter your password ").strip()
        self.banking= input("Which bank are you login into? ").lower()
        if self.banking == 'gtbank':
            self.pquerry = 'SELECT * FROM gtbank WHERE accountnumber = %s and pass_word = %s'
            self.confirm1()
        elif self.banking == 'stanbic':
             self.pquerry = 'SELECT * FROM stanbic WHERE accountnumber = %s and pass_word = %s'
             self.confirm1()
        elif self.banking == 'zenith':
             self.pquerry = 'SELECT * FROM zenith WHERE accountnumber = %s and pass_word = %s'
             self.confirm1()
             
    def confirm1(self):
        self.val = (self.user, self.passw)
        cursor.execute(self.pquerry,self.val)
        self.loginresult = cursor.fetchone()
        if self.loginresult:
            print('login succesful')
            self.homepage()
        else:
            print('invalid details, try again')
            self.login()
        
        
    def deposit(self):
        self.acc = input('what account do you want to deposit in?\n')
        self.choosing_bank = input('choose a bank to deposit into;\n1.gtbank\n2.stanbic\n3.Zenith\n')
        if self.choosing_bank == '1':
           self.query = 'SELECT * FROM gtbank WHERE accountnumber = %s'
           self.querry = 'UPDATE gtbank SET accountbalance = %s WHERE accountnumber = %s'
           self.confirm()
        elif self.choosing_bank == '2':
            self.query = 'SELECT * FROM stanbic WHERE accountnumber = %s'
            self.querry = 'UPDATE stanbic SET accountbalance = %s WHERE accountnumber = %s'
            self.confirm()
        elif self.choosing_bank == '3':
            self.query = 'SELECT * FROM zenith WHERE accountnumber = %s'
            self.querry = 'UPDATE zenith SET accountbalance = %s WHERE accountnumber = %s'
            self.confirm()
            
    def confirm(self):
        self.val =(self.acc,)
        cursor.execute(self.query,self.val)
        self.result = cursor.fetchone()
        if self.result:
            self.amount = int(input('Enter the amount you want to deposit:'))
            self.newbal = self.result[9]+ self.amount
            self.val2 = (self.newbal, self.acc)
            cursor.execute(self.querry, self.val2)
            conn.commit()
            print(f'you have successfully deposited {self.amount} to {self.result[1]}')
            self.start()
        else:
            print('account not found, try again')
            self.deposit()
               
    def homepage(self):
        self.service = input('What would you like to do?\n1.Transfer\n2.buy airtime\n3.buy data\n4. Pay utility bills\n5.Leave\n')
        if self.service == '1':
            self.transfer()
        elif self.service == '2':
                self.airtime()
        elif self.service == '3':
            self.data()
        elif self.service == '4':
            self.utility()
        else:
            print('BYE BITCH')
            
    def transfer(self):
        self.user_acc = int(input("Enter recipient's account number "))
        self.user_bank = input("Enter recipient's bank ").lower()
        if self.user_bank == "gtbank":
            self.query = 'select * from gtbank where accountnumber = %s '
            self.userbank()
        elif self.user_bank == "stanbic":
            self.query = "SELECT * FROM stanbic WHERE accountnumber = %s"
            self.userbank()
        elif self.user_bank == "zenith":
            self.query = "SELECT * FROM zenith WHERE accountnumber = %s"
            self.userbank()
            

    def userbank(self):
        self.val = (self.user_acc, )
        cursor.execute(self.query, self.val)
        self.user_result = cursor.fetchone()
        if self.user_result:
            self.amount = int(input("Enter the amount you want to transfer "))
            if self.loginresult[9] < self.amount:
                print("You're broke. Go home")
                self.homepage()
            else:
                self.new_bal = self.loginresult[9] - self.amount
                self.rec_bal = self.user_result[9] + self.amount
                self.update()
                print('Transfer successful')
                self.homepage()
   
    def update(self):
        if self.banking == "gtbank":
            self.query = 'update gtbank set accountbalance = %s where accountnumber = %s'
            self.val = (self.new_bal, self.loginresult[0])
            cursor.execute(self.query, self.val)
            conn.commit()
            if self.user_bank == "gtbank":
                self.query2 = 'update gtbank set accountbalance = %s where accountnumber = %s'
                self.val2 = (self.rec_bal, self.user_result[0])
                cursor.execute(self.query2, self.val2)
                conn.commit()
            elif self.user_bank == "stanbic":
                self.query2 = "UPDATE stanbic SET accountbalance = %s WHERE accountnumber = %s"
                self.val2 = (self.rec_bal, self.user_result[0])
                cursor.execute(self.query2, self.val2)
                conn.commit()
            elif self.user_bank == "zenith":
                self.query2 = "UPDATE zenith SET accountbalance = %s WHERE accountnumber = %s"
                self.val2 = (self.rec_bal, self.user_result[0])
                cursor.execute(self.query2, self.val2)
                conn.commit()
        elif self.banking == "stanbic":
            self.query = "UPDATE stanbic SET accountbalance = %s WHERE accountnumber = %s"
            self.val = (self.new_bal, self.loginresult[0])
            cursor.execute(self.query, self.val)
            conn.commit()
            if self.user_bank == "gtbank":
                self.query2 = 'update gtbank set accountbalance = %s where accountnumber = %s'
                self.val2 = (self.rec_bal, self.user_result[0])
                cursor.execute(self.query2, self.val2)
                conn.commit()
            elif self.user_bank == "stanbic":
                self.query2 = "UPDATE stanbic SET accountbalance = %s WHERE accountnumber = %s"
                self.val2 = (self.rec_bal, self.user_result[0])
                cursor.execute(self.query2, self.val2)
                conn.commit()
            elif self.user_bank == "zenith":
                self.query2 = "UPDATE zenith SET accountbalance = %s WHERE accountnumber = %s"
                self.val2 = (self.rec_bal, self.user_result[0])
                cursor.execute(self.query2, self.val2)
                conn.commit()
        elif self.banking == "zenith":
            self.query = "UPDATE zenith SET accountbalance = %s WHERE accountnumber = %s"
            self.val = (self.new_bal, self.loginresult[0])
            cursor.execute(self.query, self.val)
            conn.commit()
            if self.user_bank == "gtbank":
                self.query2 = 'update gtbank set accountbalance = %s where accountnumber = %s'
                self.val2 = (self.rec_bal, self.user_result[0])
                cursor.execute(self.query2, self.val2)
                conn.commit()
            elif self.user_bank == "stanbic":
                self.query2 = "UPDATE stanbic SET accountbalance = %s WHERE accountnumber = %s"
                self.val2 = (self.rec_bal, self.user_result[0])
                cursor.execute(self.query2, self.val2)
                conn.commit()
            elif self.user_bank == "zenith":
                self.query2 = "UPDATE zenith SET accountbalance = %s WHERE accountnumber = %s"
                self.val2 = (self.rec_bal, self.user_result[0])
                cursor.execute(self.query2, self.val2)
                conn.commit()
                
    def airtime(self): 
        self.network = ['mtn', 'glo', 'airtel', 'etisalat']
        self.phonenumber = input('Enter phone number:')
        while len(self.phonenumber) != 11:
            print('phone number must be 11 digits') 
            self.phonenumber = input('Enter phone number:')  
        else:
            self.line = input('Pick a network:')
            while self.line not in self.network:
                print('invalid')
                self.line = input('Pick a network:') 
            else:
                self.sent2()
    
    def sent2(self):
        self.amount = int(input('Enter amount that you want to send:'))  
        self.val = (self.user, self.passw)
        cursor.execute(self.pquerry, self.val)
        self.loginresult = cursor.fetchone()   
        while self.loginresult[9] < self.amount:
            print('You are a broke ass')
            self.amount = int(input('Enter amount that you want to send:'))
        else:
            self.newbal = self.loginresult[9] - self.amount  
            if self.banking == 'gtbank':
                self.querry = 'update gtbank SET accountbalance = %s WHERE accountnumber = %s'
                self.val = (self.newbal, self.loginresult[0])
                cursor.execute(self.querry, self.val)
                conn.commit()
            elif self.banking == 'stanbic':
                self.querry = 'update stanbic SET accountbalance = %s WHERE accountnumber = %s'
                self.val = (self.newbal, self.loginresult[0])
                cursor.execute(self.querry, self.val)
                conn.commit()
            elif self.banking == 'zenith':
                self.querry = 'update zenith SET accountbalance = %s WHERE accountnumber = %s'
                self.val = (self.newbal, self.loginresult[0])
                cursor.execute(self.querry, self.val)
                conn.commit()
            print(f'you have successfully purchased {self.amount} worth of {self.line}.')
            
    def data(self): 
        self.network = ['mtn', 'glo', 'airtel', 'etisalat']
        self.phonenumber = input('Enter phone number:')
        while len(self.phonenumber) != 11:
            print('phone number must be 11 digits') 
            self.phonenumber = input('Enter phone number:')  
        else:
            self.line = input('Pick a network:')
            while self.line not in self.network:
                print('invalid')
                self.line = input('Pick a network:') 
            else:
                self.sent3()   
                
    def sent3(self):
        self.dataplan = ("1.#300 for 1GB\n2.#1500 for 6GB\n3.#1200 for 2GB")
        print(self.dataplan)
        self.data = input('Pick a dataplan:')
        if self.data == "1":
            self.amount = 300
        elif self.data == "2":
            self.amount = 1500
        elif self.data == "3":
            self.amount = 1200   
        self.val = (self.user, self.passw)
        cursor.execute(self.pquerry, self.val)
        self.loginresult = cursor.fetchone()   
        while self.loginresult[9] < self.amount:
            print('You are a broke ass')
            self.data = input('Pick a dataplan:')
        else:
            self.newbal = self.loginresult[9] - self.amount 
            if self.banking == 'gtbank':
                self.querry = 'update gtbank SET accountbalance = %s WHERE accountnumber = %s'
                self.val = (self.newbal, self.loginresult[0])
                cursor.execute(self.querry, self.val)
                conn.commit()
            elif self.banking == 'stanbic':
                self.querry = 'update stanbic SET accountbalance = %s WHERE accountnumber = %s'
                self.val = (self.newbal, self.loginresult[0])
                cursor.execute(self.querry, self.val)
                conn.commit()
            elif self.banking == 'zenith':
                self.querry = 'update zenith SET accountbalance = %s WHERE accountnumber = %s'
                self.val = (self.newbal, self.loginresult[0])
                cursor.execute(self.querry, self.val)
                conn.commit()
            print(f'you have successfully purchased {self.amount} worth of {self.line}.')
    
    def utility(self):
        self.utilities = input('1.TV\n2.Electricity\n>>>')
        if self.utilities == '1':
            self.show = input('1.Netflix\n2.Prime\n3.Hulu\n>>>')
            self.pay_tility()
        elif self.utilities == '2':
            self.show = input('Pick one\n1. IBDEC\n2. EEDC3. IKEDC\n4. KEDCO\n>>>')
            self.pay_tility()
  
    def pay_tility(self):
        if self.show == "1" or self.show == "2" or self.show == "3" or self.show == "4":
            self.price = int(input("Enter the amount you want to pay for:>>> "))
            while self.price > self.loginresult[9]:
                print("INSUFFICENT FUNDS")
                self.price = int(input("Enter the amount you want to pay for:>>> "))
            else:
                self.newbal = self.loginresult[9] - self.price
                if self.banking == 'gtbank':
                    self.querry = 'update gtbank SET accountbalance = %s WHERE accountnumber = %s'
                    self.val = (self.newbal, self.loginresult[0])
                    cursor.execute(self.querry, self.val)
                    conn.commit()
                elif self.banking == 'stanbic':
                    self.querry = 'update stanbic SET accountbalance = %s WHERE accountnumber = %s'
                    self.val = (self.newbal, self.loginresult[0])
                    cursor.execute(self.querry, self.val)
                    conn.commit()
                elif self.banking == 'zenith':
                    self.querry = 'update zenith SET accountbalance = %s WHERE accountnumber = %s'
                    self.val = (self.newbal, self.loginresult[0])
                    cursor.execute(self.querry, self.val)
                    conn.commit()
                print("PROCESSING...")
                print(f"You have suuccessfully bought N{self.price} worth of subscription")
                
me()
        
   
