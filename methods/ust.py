arr=[100,200,300,400,500,600,700,800]


odd_position=[arr[i] for i in range(0,len(arr)) if i%2!=0]

print(odd_position)

print("op",odd_position)



for i in range(1,len(arr),2):
    
    element=odd_position.pop()

    arr[i]=element
print(arr)