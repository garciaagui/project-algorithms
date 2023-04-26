def is_palindrome_recursive(word, low_index, high_index):
    word = word.lower()

    if not len(word) or word[low_index] != word[high_index]:
        return False

    if low_index == (len(word) - 1) and high_index == 0:
        return word[low_index] == word[high_index]

    else:
        low_index += 1
        high_index -= 1
        return is_palindrome_recursive(word, low_index, high_index)
