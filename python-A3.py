print('testing testing')

## Functional Prompt 
'''
Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

'''
def flatten_sort_array(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

array_list = {'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}


print(flatten_sort_array(array_list))