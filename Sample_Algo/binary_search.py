# Time: O(log n)
import math

def binary_search(array, search):
    low = 0
    high = len(array) - 1

    while low <= high:
        middle = math.floor((low + high) / 2)
        guess = array[middle]
        if guess == search:
            return middle
        elif guess > search:
            high = middle - 1
        else: # guess < search
            low = middle + 1
    return None

def binary_search_rec(array, search):
    if len(array) == 1:
        return None
    else:
        middle = math.floor(len(array) / 2)
        if array[middle] == search:
            return search
        elif array[middle] > search:
            return binary_search_rec(array[:middle], search)
        else:
            return binary_search_rec(array[middle:], search)

arr = [r for r in range(0, 20)]
for i in range(20):
    search = binary_search(arr, i)
    if search == None:
        print("Error at {}".format(i))

x = binary_search_rec(arr, 19)
print(x)