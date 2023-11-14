def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    # O(log n)
    if right_index < left_index:
        return -1
    
    mid_index = (left_index + right_index) // 2
    
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1
    
    mid_number = numbers_list[mid_index]
    
    if mid_number == number_to_find: return mid_index
    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1
        
    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

def find_all_occurances(numbers, number_to_find):
    index = binary_search_recursive(numbers, number_to_find, 0, len(numbers))
    indeces = [index]
    
    # find indices on left hand
    i = index - 1
    while i >= 0:
        if numbers[i] == number_to_find:
            indeces.append(i)
        else:   
            break
        i = i - 1
        
    # find indices on right hand
    i = index + 1
    while i < len(numbers):
        if numbers[i] == number_to_find:
            indeces.append(i)
        else:
            break
        i = i + 1
        
    return sorted(indeces)

if __name__ == '__main__':
    numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    number_to_find = 15
    indices = find_all_occurances(numbers, number_to_find)
    print(f"Found {len(indices)} {'occurance' if len(indices) == 1 else 'occurances'} of {number_to_find}, at {'index' if len(indices) == 1 else 'indices'}: {indices}")