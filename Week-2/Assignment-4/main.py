def count(inputs):
    if not isinstance(inputs, list):
        raise ValueError('inputs is not list')
    result = {}
    for item in inputs:
        if item not in result:
            result[item] = 0
        result[item] += 1
    return result


def group_by_key(inputs):
    result = {}
    for item in inputs:
        key = item.get('key', None)
        value = item.get('value', None)
        if key is None:
            raise ValueError('missing "key"')
        if value is None:
            raise ValueError('missing "value"')
        if not isinstance(value, int) and not isinstance(value, float) :
            raise ValueError('value is not number')
        if key not in result:
            result[key] = 0
        result[key] += value
    return result


if __name__ == '__main__':
    input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
    print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}

    input2 = [
        {'key': 'a', 'value': 3},
        {'key': 'b', 'value': 1},
        {'key': 'c', 'value': 2},
        {'key': 'a', 'value': 3},
        {'key': 'c', 'value': 5}
    ]
    print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}
