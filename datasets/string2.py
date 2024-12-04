def longest_word(text):
    words = text.split()
    max_word = max(words, key=len)
    return max_word

text = "this is a simple question return word with maximum number of characters"
print(longest_word(text))