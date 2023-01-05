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

arr = [r for r in range(504928)]
for i in range(504928):
    search = binary_search(arr, i)
    if search == None:
        print("Error at {}".format(i))