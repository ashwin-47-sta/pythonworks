
prev=0

curr=1

print(prev)

print(curr)

for i in range(1,8):

    next=prev + curr
    print(next)

    prev=curr

    curr=next

    