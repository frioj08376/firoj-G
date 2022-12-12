# SUM OF N NATURAL NUMBER...

num=int(input("enter the number here....  "))
if(num<0):
    print("plz enter the positive number...")
else:
    sum=0
    while(num>0):
     sum+=num
     num-=1
    print(sum)