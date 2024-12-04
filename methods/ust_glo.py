
arr=[100,200,300,400,500,600,700,800]
#      0  1   2   3   4   5    6  7  

# #  output

# odd_position=[arr[i] for i in range(0,len(arr)) if i%2!=0]

# print(odd_position)

# print("op",odd_position)



# for i in range(1,len(arr),2):
#     element=odd_position.pop()

#     arr[i]=element
# print(arr)

odd_position_number=[num for index,num in enumerate(arr) if index%2!=0]

odd_position_number.reverse()

print(odd_position_number)

for index,num in enumerate(odd_position_number):


    arr[index+1]=num

    

print(arr)


