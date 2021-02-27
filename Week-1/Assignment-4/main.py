def binary_search_position(numbers, target):
    if len(numbers) == 0:
        return -1
    start_position = 0
    end_position = len(numbers) - 1
    while start_position != end_position:
        mid_position = (start_position + end_position) // 2
        if target == numbers[mid_position]:
            return mid_position
        elif target > numbers[mid_position]:
            start_position = mid_position + 1
        elif target < numbers[mid_position]:
            end_position = mid_position
    return -1       

if __name__ == '__main__':
    print(binary_search_position([1, 2, 5, 6, 7], 1)) # should print 0 
    print(binary_search_position([1, 2, 5, 6, 7], 6)) # should print 3
