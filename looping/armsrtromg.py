

number=int(input("enter number:"))

digit_count=len(str(number))

print(digit_count)

total=0

while(number!=0):

    digit=number%10
    exponent=digit**digit_count
    total=total+digit
    number=number//10

print(total)

