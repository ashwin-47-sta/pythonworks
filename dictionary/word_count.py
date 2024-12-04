words=["hai","hello","hai","hello","hai"]

word_count={}

for w in words:

    if w in word_count:

        word_count[w]+=1

    else:

        word_count[w]=1

print(word_count)


text="ABBACB"

char_count={}


for ch in text:

    if ch in char_count:
        char_count[ch]+=1

    else:
        char_count[ch]=1

print(char_count)
