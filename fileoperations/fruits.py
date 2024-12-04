
f=open("C:\\Users\\leoas\\OneDrive\\Desktop\\pythonworks\\datasets\\fruits.text","r")

fruits=[]

for line in f:

    fruits.append(line.rstrip("\n"))

print(fruits)