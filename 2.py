# User will input (3ages).Find the oldest one
a1 = int(input("Enter age 1: "))
a2 = int(input("Enter age 2: "))
a3 = int(input("Enter age 3: "))                    
if a1 > a2 and a1 > a3:
    print("The oldest age is:", a1)
elif a2 > a1 and a2 > a3:
    print("The oldest age is:", a2)
else:
    print("The oldest age is:", a3)