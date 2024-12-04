
def find_vowels(string):
    vowels="aeiou"
    found_vowels=[char for char in string if char in vowels]

    return found_vowels

print(find_vowels("priya"))