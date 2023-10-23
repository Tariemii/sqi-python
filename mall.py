import time
import random
import mysql.connector 
conn = mysql.connector.connect(host = "127.0.0.1", user = 'root', password = "", database = "MALL")
cursor = conn.cursor()


class mall:
    def __init__(self):
        print('Welcome to the MALL!!!')
        self.cat = {}
        self.cart = {}
        self.prices = {}
        self.validate = False
        self.start()
        
    
    def start(self):
        self.home = input('What would you like to do?\n1.Go to homepage\n2.Login\n3.Register\n4.Checkout\n5.Exit\n>>>')
        if self.home == '1':
            self.homepage()
        elif self.home == '2':
            self.login()
        elif self.home == '3':
            self.register()
        elif self.home == '4':
            self.checkout()
        else:
            print('Thanks for using our services and have a great day')
         
         
    def homepage(self):
        self.category = ['computers', 'drinks', 'home', 'fashion', 'toiletries', 'wares']
        self.pick = input(f'What would you like to get?\nPick a category you would like to check out:{self.category}\n').lower()
        if self.pick in self.category:
            if self.pick == 'fashion':
                self.pick = input('Select men or women: ').lower()
                if self.pick != 'men' and self.pick != 'women':
                  print('Category not available, Try again.')
                  self.homepage()  
            self.query = f'SELECT productname from {self.pick}'
            cursor.execute(self.query)
            self.presult = cursor.fetchall()
            if self.presult:
                self.product()
        else:
            time.sleep(1)
            print('Category not available, Try again.')
            self.homepage()
            
    def product(self):
        print(f'These are the products available under this category:{self.presult}') 
        self.products = input('What would you like to pick?\n').lower()
        self.querry = f"SELECT * FROM {self.pick} WHERE productname = {'%s'}"
        self.val = (self.products,)
        cursor.execute(self.querry, self.val)
        self.result = cursor.fetchone()
        if self.result:
            if self.result[3] == 0:
                print('Product unavailable for the moment')
                self.product()
            print(f'The current price of {self.products} is ₦{self.result[2]} and there are {self.result[3]} available')
            self.many = int(input('How many would you like to purchase\n>>>'))
            while self.many > self.result[3]:
                print('This amount is not available. Try again')
                self.many = input('How many would you like to purchase\n>>>')
            else:
                self.price = self.result[2] * self.many
                if self.many >= 10:
                    self.newprice = self.price - (self.price * 0.1)
                    print(f'The price is {self.price} but you have a 10% discount and the price is {self.newprice}')
                    self.prices.update({self.products:self.newprice})
                else:
                    print(f'The price is {self.price}')
                    self.prices.update({self.products:self.price})
                self.cart.update({self.products: self.many})
                self.cat.update({self.pick: self.cart})
                
                print('You have successfully added the item(s) to the cart')
                self.again = input('1.checkout\n2.Add more items to cart\n3.To go back home\n>>>')
                if self.again == '1':
                    self.cart = {}
                    self.checkout()
                elif self.again == '2':
                    self.product()
                elif self.again == '3':
                    self.cart = {}
                    self.homepage()
                else:
                    print('Goodbye')
        else:
            print('This product is not available. TRY AGAIN!!!')
            self.product()
     
    def checkout(self):
        if len(self.cat) == 0:
            print('There are no items in your cart')
            time.sleep(2)
            self.homepage()
        else:
            print(f'{self.cat} are the items you have in your cart') 
            if self.validate == False:
                print('You are not logged in yet')
                time.sleep(2)
                self.login()
            else:
                for cat in self.cat:
                    for item in self.cat[cat]:
                        self.querry = f'select * from {cat} where productname = {"%s"}'
                        self.val = (item,)
                        cursor.execute(self.querry, self.val)
                        self.result = cursor.fetchone()
                        self.newqua = self.result[3] - self.cat[cat][item] 
                        self.querry2 = f'update {cat} set quantity = {"%s"} where productname = {"%s"}'
                        self.val2 = (self.newqua, item)
                        cursor.execute(self.querry2, self.val2)
                        conn.commit()
                        self.querry3 = 'insert into sales (orderid, customer_name, product, price, quantity) values(%s, %s, %s, %s, %s)'
                        self.val3 = (random.randrange(1000, 9000), self.user, item, self.prices[item], self.cat[cat][item] )
                        cursor.execute(self.querry3, self.val3)
                        conn.commit()
                time.sleep(1)
                self.done = input('Checkout successful\n1.Shop again\n2.LEAVE\n>>>')
                if self.done == '1':
                    self.homepage()
                else:
                    time.sleep(1)
                    print('Thanks for using our services, Goodbye')
                  
    def register(self):
        self.user_info = []
        self.information = ['first name', 'last name', 'Age', 'Gender', 'Address', 'Phonenumber','Password', 'email', 'accountnumber']
        for info in self.information:
            decision = input(f'Enter your {info}:')
            while info == 'Phonenumber' and len(decision) != 11:
                print('Phone number must be 11 digits')
                decision = input(f'Enter your {info}:')
            self.user_info.append(decision)
        self.username = self.user_info[0][0:3] + str(random.randrange(100, 999))
        self.user_info.append(self.username)
        print(f'Your username is {self.username} and your password is {self.user_info[6]}')
        self.val = tuple(self.user_info)
        self.querrry = 'insert into register (fname, lname, Age, Gender, Address, phonenumber, pass_word, email, accountnumber, username) values (%s, %s, %s,%s, %s, %s, %s, %s, %s, %s)' 
        cursor.execute(self.querrry, self.val)
        conn.commit()
        print('Processing...')
        time.sleep(1)
        print('Registration successful')
        print('redirecting...')
        time.sleep(1)
        self.homepage()
        
        
    def login(self):
        self.user = input('Enter your username: ')
        self.password = input('Enter your password: ')
        self.querr = 'select * from register where username = %s and pass_word = %s'
        self.val = (self.user, self.password)
        cursor.execute(self.querr, self.val)
        self.result = cursor.fetchone()
        if self.result:
            print('Processing..')
            time.sleep(1)
            print('Login successful')
            self.add = input('1. Go to homepage\n2. Checkout\n3.Logout\n>>>')
            self.validate = True
            if self.add == '1':
                self.homepage()
            elif self.add == '2':
                self.checkout()
            else:
                self.validate = False
                self.start() 
        else:
            self.retry = input('Invalid login details\nEnter 1 to try again\nEnter 2 to register\n>>>')
            if self.retry == '1':
                self.login()
            elif self.retry == '2':
                self.register()
            else:
                print('Byeeee')
mall()