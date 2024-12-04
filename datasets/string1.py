# the count of alphabets


text="on june 5th, 2024, we will celebrate @ our annual event:'Tech Innovation 2024!"

alphabet_count = sum(char.isalpha() for char in text)

print("Number of alphabetic characters:",(alphabet_count))

#count of space

text="on june 5th, 2024, we will celebrate @ our annual event:'Tech Innovation 2024!"

space_count=text.count(' ')

print("number of space count",space_count)

#count of special characters

text = "On June 5th, 2024, we will celebrate @ our annual event: 'Tech Innovations 2024!'"
special_char_count = sum(1 for char in text if not char.isalnum() and not char.isspace())
print(special_char_count)

#count of count of number


text="on june 5th, 2024, we will celebrate @ our annual event:'Tech Innovation 2024!"

number_count=sum(1 for cha in text  if cha.isdigit())

print("number count => ",number_count)