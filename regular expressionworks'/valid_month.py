
from re import fullmatch

month=input("enter the date:")

pattern="([1-9]|0[1-9]|1[0-2])"

matcher=fullmatch(pattern,month)

if matcher==None:

    print("invalid")

else:

    print("valid")
