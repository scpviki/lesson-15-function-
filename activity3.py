def add(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def divide(a,b):
    return a/b
print("select an operation")
print("press a for addition")
print("press b for subtraction")
print("press c for nmultiplication")
print("press d for division")   
choice=input("please enter your choice")
numm1=int (input("please enter number 1"))
numm2=int (input("please enter number 2"))
if choice=="a":
    print(f"{numm1} + {numm2} ={add(numm1,numm2)}")
elif choice=="b":
    print(f"{numm1} - {numm2} ={subtraction(numm1,numm2)}")
elif choice=="c":
    print(f"{numm1} * {numm2} ={multiplication(numm1,numm2)}")
elif choice=="d":
    print(f"{numm1} / {numm2} ={divide(numm1,numm2)}")
else:
    print("invalid input")