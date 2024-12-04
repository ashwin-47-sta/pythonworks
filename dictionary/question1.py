

arr=[10,20,30,40,2,3,7,8,9]

frequency_count={num:arr.count(num) for num in arr}

print(frequency_count)
# result={num:num**3 for num in arr}
# result={key:values iteration condition}

# for num in arr:

#     square=num**2
#     result[num]=square

# print(result)

# even_squares={num:num**2 for num in arr if num%2==0}
# print(even_squares)

# odd_cubes={num:num**3 for num in arr if num%2!=0}
# print(odd_cubes)