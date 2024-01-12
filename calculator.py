
print("\t\tWellcome to Calculator")
num1=input("Enter the First Number \n")
num2=input("Enter the second Number \n")
num3=input("enter the operator\n")
if num3=='+':
    print(int(num1) + int(num2))
elif num3=='-':
    print(int(num1) - int(num2))
elif num3=='/':
    print(int(num1) / int(num2))
elif num3=='*':
    print(int(num1) * int(num2))
else:
    print("Enter the valid operation")

  