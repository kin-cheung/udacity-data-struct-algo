def merge_sort(input_list):
    n = len(input_list)
    if n == 1 :
        return input_list
    
    if n == 2 :
        if input_list[0] > input_list[1] :
            return [input_list[1], input_list[0]]
    
    mid = int(n / 2)
    left = merge_sort(input_list[:mid])
    right = merge_sort(input_list[mid:])
    
    i, j = 0, 0
    output = []
    while i < len(left) and j < len(right) :
        if left[i] < right[j] :
            output.append(left[i])
            i += 1
        else :
            output.append(right[j])
            j += 1
    
    if i < j :
        [output.append(x) for x in left[i:]]
    else :
        [output.append(y) for y in right[j:]]
    
    return output
    

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_list = merge_sort(input_list)
    
    ans1, ans2 = 0, 0
    multiplier = 1
    
    for i, n in enumerate(sorted_list) :
        if i % 2 == 1 :
            ans1 += n * multiplier
            multiplier *= 10
        else :
            ans2 += n * multiplier
    
    return [ans1, ans2]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

print(rearrange_digits([1, 2, 3, 4, 5]))
# [42, 531]
print(rearrange_digits([4, 6, 2, 5, 9, 8]))
# [964, 852]
print(rearrange_digits([2, 1, 1, 2]))
# [21, 21]
print(rearrange_digits([0]))
# [0, 0]