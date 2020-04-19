def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    n = len(input_list)
    a = [0] * 3
    
    for e in input_list :
        a[e] += 1
    
    ans = []
    for i, x in enumerate(a) :
        for _ in range(x) :
            ans.append(i)
    
    return ans

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")
        

print(sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]))
# [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
print(sort_012([0, 1, 2]))
# [0, 1, 2]
print(sort_012([2, 2, 2, 1, 1, 1, 0, 0, 0]))
# [0, 0, 0, 1, 1, 1, 2, 2, 2]
print(sort_012([]))
# []
print(sort_012([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]