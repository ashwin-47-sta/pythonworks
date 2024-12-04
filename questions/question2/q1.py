


# the count of alphabets


text="on june 5th, 2024, we will celebrate @ our annual event:'Tech Innovation 2024!"

alphabet_count = sum(char.isalpha() for char in text)

print("Number of alphabetic characters:",(alphabet_count))

#count of space


space_count=text.count(' ')

print("number of space count",space_count)

# count of number



number_count=sum(1 for cha in text  if cha.isdigit())

print("number count => ",number_count)



# special characters

count=0

for char in text :

    if not char.isalnum() and not char.isspace():

        count+=1
        
print(count)
