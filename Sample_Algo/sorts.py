import random
import copy

# Time: O(n^2)
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

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


arr = [random.randint(-100, 100) for i in range(10)]
sorted = quicksort(arr)
print(sorted)
        
        
            

