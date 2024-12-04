

number=int(input("enter number:"))

prev=0

curr=1

is_fibo=False 

for i in range(1,number+1):

    next=prev+curr

    prev=curr

    curr=next

    if next==number:

        is_fibo=True

        break

print(is_fibo)    