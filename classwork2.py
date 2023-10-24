"""
run a loop that wil go for 6 times, asking for the following information: fname, lnam, mname, age, gender, level
"""
info = []
values = []

for i in range(6):
    information = input('Enter information:')
    value = input('Enter value:')
    info.append(information)
    values.append(value)
first = {info:value}
print(first)

info = {}
for i in range(6):
    information = input()
    valu = input()
    info[information] = valu
    print(info)
   