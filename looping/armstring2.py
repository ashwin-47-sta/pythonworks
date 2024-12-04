number=int(input("enter number"))


original = number

digit_count=len(str(number))

total=0

while(number!=0):

    digit=number%10

    exponent=digit**digit_count

    number=number//10

print("armstring number"if total==original else "not armstring number")

