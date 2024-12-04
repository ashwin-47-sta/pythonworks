def swap_dec(fn):
     def wrapper(n1,n2):
         
         if n1<n2:
             (n1,n2)=(n2,n1)
         return fn(n1,n2)


     return wrapper

def round_dec(fn):

    def wrapper(num1,num2):

        num1=round(num1)

        num2=round(num2)

        return fn (num1,num2)
    return wrapper

@round_dec
@swap_dec
def add_number(num1,num2):
    
    return num1+num2

@round_dec
@swap_dec
def subtraction(num1,num2):

    return num1-num2

@round_dec
@swap_dec
def divison(num1,num2):

    return num1/num2

@round_dec
@swap_dec

def multiplication(num1,num2):

    return num1*num2


print(multiplication(2,19))