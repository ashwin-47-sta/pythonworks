text="this is a simple python program that print most recursive word . this program is simple" 


words=text.split(" ")

def get_count(w):

    return words.count(w)

frequent_word=max(words,key=get_count)

print(frequent_word)