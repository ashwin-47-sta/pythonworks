

from re import fullmatch


gmail=input("enter the gmail:")

pattern="[a-z]+[a-z0-9]{5,63}@gmail.com"

matcher=fullmatch(pattern,gmail)

print("invalid" if  matcher==None else "valid")