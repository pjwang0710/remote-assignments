
def find_max(numbers):
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number

# your code here
def find_position(numbers, target):
    position = -1
    for i, num in enumerate(numbers):
        if num == target:
            position = i
            break
    return position

# your code here
if __name__ == '__main__':
    print(find_max([1, 2, 4, 5]) ); # should print 5
    print(find_max([5, 2, 7, 1, 6]) ); # should print 7
    print(find_position([5, 2, 7, 1, 6], 5)) # should print 0 
    print(find_position([5, 2, 7, 1, 6], 7)) # should print 2 
    print(find_position([5, 2, 7, 7, 7, 1, 6], 7)) # should print 2 (the first one) 
    print(find_position([5, 2, 7, 1, 6], 8)) # should print -1