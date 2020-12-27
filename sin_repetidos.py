def without_repeating(list):
    result = []
    for element in list:
        if element not in result:
            result.append(element)
    return result


one_list = without_repeating([1, 2, 1, 3, 2])

print(one_list)
