# armstrong number program for 3 digit.

num=int(input("enter the number..."))
sum=0
temp=num
while(temp>0):
    digit= temp%10
    cube=digit**3
    sum=sum+cube
    temp//=10
if(sum==num):
 print("it is an armstrong number")

else:
      print("it is not an armstrong number")