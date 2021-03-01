def binary_search_last(numbers, target):
    if len(numbers) == 0:
        return -1
    start_position = 0
    end_position = len(numbers) - 1
    while start_position <= end_position:
        mid_position = (start_position + end_position) // 2
        if target >= numbers[mid_position]:
            start_position = mid_position + 1
        elif target < numbers[mid_position]:
            end_position = mid_position - 1
    return start_position

def binary_search_first(numbers, target):
    if len(numbers) == 0:
        return -1
    start_position = 0
    end_position = len(numbers) - 1
    while start_position <= end_position:
        mid_position = (start_position + end_position) // 2
        if target > numbers[mid_position]:
            start_position = mid_position + 1
        elif target <= numbers[mid_position]:
            end_position = mid_position - 1
    return end_position + 1

def binary_search(method):
    test_array = [
        ([1, 2, 5, 5, 5, 6, 7], 2),
        ([1, 2, 5, 5, 5, 6, 7], 5),
        ([1, 2, 5, 5, 5, 6, 7], 3),
        ([1, 2, 5, 5, 5, 6, 7], 0),
        ([1, 2, 5, 5, 5, 6, 7], 1.5),
        ([1, 2, 5, 5, 5, 6, 7], 3),
        ([1, 2, 5, 5, 5, 6, 7], 4),
        ([1, 2, 5, 5, 5, 6, 7], 5.5),
        ([1, 2, 5, 5, 5, 6, 7], 6.5),
        ([1, 2, 5, 5, 5, 6, 7], 8)
    ]
    for test_item in test_array:
        if method == 'first':
            print(binary_search_first(test_item[0], test_item[1]))
        elif method == 'last':
            print(binary_search_last(test_item[0], test_item[1]))

if __name__ == '__main__':
    binary_search('first')
    # binary_search('last')