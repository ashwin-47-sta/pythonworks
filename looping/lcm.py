a=int (input("enter number:"))
b=int(input("enter number:"))
#lcm=(x*y)//compute_gcd(x,y)

if a>b:
    greater=a
else:

    greater=b

while(True):

    if greater%a==0:
        lcm=greater
        break
    greater+=1

print(lcm)

