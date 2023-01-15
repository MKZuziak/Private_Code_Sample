from helpers import compare_results
import random
def sum_array(array):
    if len(array) == 1:
        return array[0]
    else:
        return array[0] + sum_array(array[1:])

def count_array(array):
    if len(array) == 1:
        return 1
    else:
        return 1 + count_array(array[1:])

def find_largest(array):
    if len(array) == 1:
        return array[0]
    else:
        candidate = find_largest(array[1:])
        if candidate > array[0]:
            return candidate
        else:
            return array[0]

arr = [random.randint(-10000, 10000) for x in range(100)]
compare_results(func = sum_array, func_built = sum, array = arr)
compare_results(func = count_array, func_built= len, array=arr)
compare_results(func = find_largest, func_built= max, array= arr)