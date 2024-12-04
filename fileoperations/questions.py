
f=open("C:\\Users\\leoas\\OneDrive\\Desktop\\pythonworks\\datasets\\questions.txt'","r")

words=[]

for line in f:

    line=line.rstrip("\n")
    all_words=line.split(" ")

    for w in all_words:
        words.append(w)

print(words)

word_count={w:words.count(w) for w in words}
nested_word_count=[[v,k] for k,v in word_count.items()]

print(sorted(nested_word_count,reverse=True))