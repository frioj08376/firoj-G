# factorial of the number.

num=int(input("Enter the number here...."))
fact=1
if(num<0):
    print("Negative number factorial's does not exist")
if(num==0):
        print("factorial of zero is", 1)
if(num>0):
    for i in range(1,num+1):
      fact=fact*i
    print("the factorial of given number is", fact)
