
text="ABAABBC"


def get_count(ch):

    return text.count(ch)

most_frequent=max(text,key=get_count)
print(most_frequent)

least_recursive_character=min(text,key=get_count)
print(least_recursive_character)