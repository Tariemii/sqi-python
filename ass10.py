"""
create a school score gradin app that will have ca1, ca2 and exam
if the score is 75 and above grade the person A
if the score is 60 but less than 75 givr the person B
if the score is 50 but less than 60 give the person C
id the score is 50 but less than 40 give the person d
if the score is below 40 give the person f
"""
test1 = float(input("Enter the first test score: "))
test2 = float(input("Enter the second test score:"))
exam = float(input('Enter exam score:'))
total = test1 + test2 + exam
print("sum:", total)

if total >= 75  :
      print('Your grade is A')
elif total >= 60 and total <=74 :
       print("Your grade is B")
elif total >= 50 and total <= 59:
        print('Your grade is C')
elif total >= 40 and total <= 49:
        print('Your grade is D')
else:
        print('Your grade is F')

