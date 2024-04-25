def print_upper_words(words, must_start_with=None):
    for word in words:
        if must_start_with is None or any(word.startswith(letter) for letter in must_start_with):
            print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})