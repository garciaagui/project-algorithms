def merge_sort(str_list, start=0, end=None):
    if end is None:
        end = len(str_list)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(str_list, start, mid)
        merge_sort(str_list, mid, end)
        merge(str_list, start, mid, end)


def merge(str_list, start, mid, end):
    left = str_list[start:mid]
    right = str_list[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            str_list[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            str_list[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            str_list[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            str_list[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    first_string_list = list(first_string.lower())
    second_string_list = list(second_string.lower())

    merge_sort(first_string_list)
    merge_sort(second_string_list)

    first_string_sorted = "".join(first_string_list)
    second_string_sorted = "".join(second_string_list)
    boolean_value = bool

    if not len(first_string_sorted) or not len(second_string_sorted):
        boolean_value = False

    else:
        boolean_value = first_string_sorted == second_string_sorted

    return (first_string_sorted, second_string_sorted, boolean_value)


print((is_anagram("roma", "amor")))
