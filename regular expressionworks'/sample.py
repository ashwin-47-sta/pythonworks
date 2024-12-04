

from re import fullmatch,findall,finditer

f=open("C:\\Users\\leoas\\OneDrive\\Desktop\\pythonworks\\datasets\\sample (1).txt")

content=f.read()

pattern="https?://[\w\s./]+"


urls=findall(pattern,content)

for url in urls:

    print(url)



