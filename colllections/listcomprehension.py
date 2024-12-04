

arr=[2,3,4,5,6,7,8,]

squares=[num**2 for num in arr]

print(squares)


evn_number=[num for num in arr if num%2==0]

print(evn_number)

add_ten=[num+10 for num in arr]
# # [return iteration condition]
print(add_ten)

odd_numbers=[num for num in arr if num%2!=0]

print(odd_numbers)

num_gt_five=[num for num in arr if num>5]

print(num_gt_five)

map_num=[num+1 if num>5 else num-1 for num in arr]

print(map_num)

text=["apple","iphone","orange","potatto","tomatto"]

# words  starting with vowels


vowels_words=[w for w in text if w[0] in ['a','e','i','o','u']]
print(vowels_words)

consonant_words=[w for w in text if w[0] not in ['a','e','i','o','u']]
print(consonant_words)

# longest words

long=max([len(w) for w in text])

longest_words=[w for w in text if len(w)==long]
print(longest_words)
