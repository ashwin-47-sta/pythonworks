text="this is a simple programming to find word with a maximum number of character "

words=text.split(" ")

def get_length(w):

    return len(w)

srt_words=sorted(words,key=get_length,reverse=True)
print(srt_words)

def get_count(w):

    return words.count(w)

frequent_word=max(words,key=get_count)

print(frequent_word)