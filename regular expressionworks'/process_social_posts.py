
from re import finditer

f=open("C:\\Users\\leoas\\OneDrive\\Desktop\\pythonworks\\datasets\\social_posts.txt")

for line in f:

    words=line.rstrip("\n")

    pattern="#\w+"

    matcher=finditer(pattern,words)

    for obj in matcher:

        print(obj.group())