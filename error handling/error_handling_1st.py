# try
# except
# finally
# raise

num1=int(input("enter num"))
num2=int(input("enter num"))

try:

    result=num1/num2

    print(result)

except:

    num2=int(input("enter number2:"))

    result=num1/num2

    print(result)

finally:


    print("file operation")

    print("db commit")



