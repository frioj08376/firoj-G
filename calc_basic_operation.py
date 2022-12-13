print(".....MINI CALCULATOR.....")
num1= float(input("enter the first number  "))
num2= float(input("enter the second the number  "))
print("press 1 for addtion \npress 2 for subtraction \npress for division \npress 4 for multiply" )
choice=int(input(" enter your choice from 1 to 4 \n "))
if choice==1:
    print(num1+num2)
elif choice==2:
    print(num1-num2)
elif choice==3:
    print(num1/num2)
elif choice==4:
    print(num1*num2)
else:
    print("invalid choice")



