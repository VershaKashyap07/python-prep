def flatten(nested_list):
    flat_list = []
    for element in nested_list:
        if isinstance(element, list):
            flat_list.extend(flatten(element))
        else:
            flat_list.append(element)
    return flat_list

# Example usage
nested_list = [[1, 2], 1, [2, [3, 4]]]
flattened_list = flatten(nested_list)
print(flattened_list)
