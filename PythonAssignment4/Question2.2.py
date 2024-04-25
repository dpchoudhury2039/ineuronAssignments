def is_vowel(char):
    # Check if the given character is a vowel
    vowels = {'a', 'e', 'i', 'o', 'u'}
    if char.lower() in vowels:
        return True
    else:
        return False


characters = ['a', 'u', 'b', 'e', 'x', 'o', 'U']
results = {char: is_vowel(char) for char in characters}

print("Character to Vowel Status:")
for char, result in results.items():
    print(f"{char}: {'Vowel' if result else 'Not a Vowel'}")
