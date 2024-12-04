

add=lambda n1, n2 :n1+n2

print(add(10,20))


sub=lambda n1,n2:n1-n2
print(sub(10,2))


cube=lambda n:n**3
print(cube(4))

max_two=lambda str1,str2:str1 if len(str1)>len(str2) else str2

# print((max_two("hai","morning")))

# words=["hallo","hai","morning","test"]

# get_length=lambda word:len(word)

# print(max(words,key=get_length))

word=["hello","hai","morning","test","apple"]

def get_length(w):

    return len(w)


srt_wors=sorted(word,key=get_length,reverse=True)
print(srt_wors)


