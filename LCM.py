a=int(input("enter the first number  \n"))
b=int(input("enter the second number   \n"))
maxNum=max(a,b)
while(True):
    if(maxNum%a==0 and maxNum%b==0):
        break
        maxNum=maxNUM+1
print(f" the lcm of {a} and {b} is {maxNum}")

