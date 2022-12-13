#HCF OF THE GIVEN NUMBERS
def hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
         if((x%i==0)and(y%i==0)):
           hcf=i
    return hcf
print("the hcf of given number is",hcf(12,30))


