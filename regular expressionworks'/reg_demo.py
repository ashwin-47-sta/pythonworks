from re import finditer


text=" i have 3 cars ,2 bike and 1 cycle"


# pattern="[a-zA-Z0-9]"
pattern="[a-z]"


matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())




