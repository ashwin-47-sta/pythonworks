



number=int(input("enter  number:"))

total=0


while(number!=0):

    digit=number %10

    total=total+digit

    print(total)

    number=number //10

print(total)
