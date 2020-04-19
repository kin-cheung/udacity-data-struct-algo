def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    n = len(input_list)
    if n == 0 :
        return -1
    
    if input_list[0] == number :
        return 0
    
    if n == 1 :
        return -1
    
    if input_list[1] == number :
        return 1
    
    if n == 2 :
        return -1
    
    mid = int(n / 2)
    if ((input_list[0] < input_list[mid - 1]) and (input_list[0] <= number <= input_list[mid - 1])) or \
       ((input_list[mid] < input_list[n - 1]) and not ( input_list[mid] <= number <= input_list[n - 1])):
        return rotated_array_search(input_list[:mid], number)
    else :
        i = rotated_array_search(input_list[mid:], number)
        if i == -1 :
            return -1
        else:
            return mid + i

        
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6))
# 0
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1))
# 5
print(rotated_array_search([6], 8))
# -1
print(rotated_array_search([], 0))
# -1