import random
import time

def binary_search_recursive(numbers, start_position, end_position, target):
    if start_position == end_position:
        if numbers[start_position] == target:
            return start_position
        else:
            return -1
    mid_position = (start_position + end_position) // 2
    if target == numbers[mid_position]:
        return mid_position
    elif target > numbers[mid_position]:
        return binary_search_recursive(numbers, mid_position+1, end_position, target)
    else:
        return binary_search_recursive(numbers, start_position, mid_position, target)

def bianry_search_iterative(numbers, target):
    start_position = 0
    end_position = len(numbers) - 1
    while start_position != end_position:
        mid_position = (start_position + end_position) // 2
        if target == numbers[mid_position]:
            start_position = mid_position
            break
        elif target > numbers[mid_position]:
            start_position = mid_position + 1
        elif target < numbers[mid_position]:
            end_position = mid_position
    if numbers[start_position] == target:
        return start_position
    return -1

def find_position_answer(numbers, target):
    try:
        position = numbers.index(target)
    except Exception as e:
        position = -1
    return position

def binary_search_position(numbers, target):
    if len(numbers) == 0:
        return -1
    time_start = time.time()
    answer = find_position_answer(numbers, target)
    built_it_function_time = time.time() - time_start
    time_start = time.time()
    iteration_solution = bianry_search_iterative(numbers, target)
    iteration_time = time.time() - time_start
    time_start = time.time()
    recursive_solution = binary_search_recursive(numbers, 0, len(numbers)-1, target)
    recursive_time = time.time() - time_start
    if iteration_solution != recursive_solution and answer != iteration_solution:
        raise ValueError('something wrong')
    print('length: {}, built-it: {:.7f}, iteration: {:.7f}, recursive: {:.7f}'.format(len(numbers), built_it_function_time, iteration_time, recursive_time))
    return recursive_solution

def get_random_array(array_length):
    random_array = []
    while len(random_array) < array_length:
        rand_num = random.randint(-10000, 10000)
        try:
            random_array.index(rand_num)
        except Exception as e:
            random_array.append(rand_num)
    rand_position = random.randint(0, max(0, array_length-1))
    return sorted(random_array), random_array[rand_position] + random.randint(0,1)
        

if __name__ == '__main__':
    for test_round in range(100):
        rand_length = random.randint(10, 1000)
        random_array, random_target = get_random_array(rand_length)
        try:
            print(binary_search_position(random_array, random_target))
        except Exception as e:
            print(str(e))
