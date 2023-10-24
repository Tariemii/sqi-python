"""
write a simple program that will ask user to supply 3 sets
when the three sets are supplied the user should be able to perform the following operation:
1. union
2. intersection
3. symmetric difference
"""
s1, s2, s3 = [], [],[]
for i in range(4):
    se1 = input('Enter the first set:')
    se2 = input('Enter your second set:')
    se3 = input('Enter the third set:')
    s1.append(se1)
    s2.append(se2)
    s3.append(se3)
set1, set2, set3 = set(s1), set(s2), set(s3)
operation = input("""Choose operation to perform
                  Enter 1 for union
                  Enter 2 for intersection
                  Enter 3 for symmetric difference:
                  """)
if operation == "1":
    set4 =set1.union(set2).union(set3)
    print(set4)
elif operation == '2':
    set4 = set1.intersection(set2).intersection(set3)
    print(set4)
elif operation == '3':
    set4 = set1.symmetric_difference(set2).symmetric_difference(set3)
    print(set4)