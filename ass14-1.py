"""
create a to-do list 
if the user enters any day of the week it should print the activities of the day
"""
days_of_the_week = {
    'monday':['Go to the market', 'get a new bible'],
    'tuesday':['get a kindle', 'go to the orphanage'],
    'wednesday': ['get married', 'have a baby'],
    'thursday' : ['get a job', 'eat cookies'],
    'friday' : ['go for vigil', 'go to the club'],
    'saturday' :['sleep in', 'babysit'],
    'sunday' : ['go to church', 'get ready for monday']
}

def todo():
    decision = input('What would you like to do today?\n1.Update your todo\n2.Check out your todo\n3.Exit the todo\n ')
    if decision == '1':
        update_todo()
    elif decision == '2':
        list_todo()
    elif decision == '3':
        print('Byeeee')
        
def update_todo():
   response = input('Enter the day you would like to update: ').lower()
   if response in days_of_the_week:
        va = input('Enter the activity you would like to add: ')
        days_of_the_week[response].append(va)
        print('You have successfully added it')
        retry = input('Enter 1 to add again or 2 to go back home: ')
        if retry == '1':
            update_todo()
        elif retry == '2':
            todo()
   else:
        print("That's not a valid day of the week. Try again")
        update_todo()
        
def list_todo():
    dec = input('What day would you like to view?\n').lower()
    if dec in days_of_the_week:
        for i in days_of_the_week[dec]:
            print(i) 
        retry = input('Enter 1 to view another todo or 2 to go back home: ')
        if retry == '1':
            list_todo()
        elif retry == '2':
            todo()
    else:
        print("That's not a valid day of the week. Try again") 
        list_todo()

todo()
          