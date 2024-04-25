def filter_long_words(words, check_length):
    longer_words = []
    for word in words:
        if len(word) > check_length:
            longer_words.append(word)
    return longer_words


word_list = ["Ineuron", "python", "cherry", "data", "blueberry", "fish", "grape"]
n = 5

longer_words = filter_long_words(word_list, n)

print(f"Words longer than {n} characters: {longer_words}")
