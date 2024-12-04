
text="ABABBCCDDE"

character_frquency={ch:text.count(ch)for ch in text}

print(character_frquency)

non_recursive_character=[k for k,v in character_frquency.items() if v==1]

print(non_recursive_character)