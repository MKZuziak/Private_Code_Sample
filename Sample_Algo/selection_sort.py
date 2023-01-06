# Time: O(n^2)
import copy

def selection_sort(array, order='desc'):
    # Note that copy operation has average case of O(n) in Python
    # We can omit making the copy, but then the original (global) array will be consumed.
    # array_copy = copy.deepcopy(array)
    sorted_array = list()
    if order == 'desc':
        while len(array) != 0:
            highesst_value = array[0]
            index_of_interest = 0
            for index_item, item in enumerate(array):
                if item > highesst_value:
                    highesst_value = item
                    index_of_interest = index_item
            sorted_array.append(highesst_value)
            del array[index_of_interest]
    else:
        while len(array) != 0:
            lowest_value = array[0]
            index_of_interest = 0
            for index_item, item in enumerate(array):
                if item < lowest_value:
                    lowest_value = item
                    index_of_interest = index_item
            sorted_array.append(lowest_value)
            del array[index_of_interest]
    return sorted_array

arr = [3, 2, 3, 1, 4, 5, 2, 2, 5, 3, 12, 5, 4, 2, -4, -1, -4, -2, -7, -2, -21]
sorted = selection_sort(arr, order='asc')
print(sorted)
        
        
            

