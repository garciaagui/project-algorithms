def is_palindrome_iterative(word):
    if not len(word):
        return False

    word = word.lower()
    low_index = 0
    high_index = len(word) - 1

    while low_index < (len(word) - 1) and high_index > 0:
        if word[low_index] != word[high_index]:
            return False

        low_index += 1
        high_index -= 1

    return True
