def twoSum(nums, target):
    buckets = {}
    for i, num in enumerate(nums):
        buckets[num] = i

    results = []
    for i, num in enumerate(nums):
        target_index = buckets.get(target-num, None)
        if target_index != None and target_index > i :
            results.append([i, target_index])
    if len(results) == 0:
        raise ValueError('cannot find solution')
    elif len(results) >= 2:
        raise ValueError(f'Got {len(results)} solutions')
    return results[0]
    

if __name__ == '__main__':
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    print(twoSum([2, 7, 11, 15], 19))
    print(twoSum([2, 7, 11, 15], 17))
    print(twoSum([2, 7, 11, 15], 18))
    print(twoSum([2, 7, 11, 15], 22))
    print(twoSum([2, 7, 11, 15], 26))
    print(twoSum([2, 7, 7, 15], 14))
    print(twoSum([2, 7, 7, 15], 22))
    print(twoSum([7, 7, 2, 15], 9))
    print(twoSum([7, 7, 7, 15], 14))
    
        