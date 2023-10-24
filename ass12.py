import random
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
    matricno = random.randrange(123456, 678910)
    endchar = 'sqi'
    matricnumber = str(matricno)+endchar
    myvalue.append(matricnumber)
    et.update({mykey:myvalue}) #et[mykey] = myvalue
    mykey = input('Enter start to register or stop to quit')
else:
    print('Registration done')
    print( "All students information:\n", et)
    
    