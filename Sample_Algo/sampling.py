import random

# This is my own implemantation of the random.choices and
# random.sample function from python.
# We select a number between 0 and |N| - 1 from the array.
# We repeat this operation K times and we return the sample.
def random_sampling(array, size, replacement=True):
    if replacement == True:
        return [array[random.randint(0, len(array) - 1)] for i in range(size)]

# Reservoir sampling allows us to collect an evenly distributed sample
# without prior knwoledge of the length of the array.
# This function represents unweighted version of reservoir sampling.
def reservoir_sampling(array, size):
    sample = []
    i = 0
    while i < size: # We want to first construct our reservoir of size == sample size.
        try: # Try and except statement if size(array) < size(sample)
            sample.append(array[i])
            i += 1
        except:
            print("Finished sampling at element {}".format(i))
            return sample
    while True:
        try:
            alpha = size / i
            if alpha > random.uniform(0, 1):
                replace = random.randint(0, size-1)
                sample[replace] = array[i]
                i += 1
            else:
                i += 1
        except:
            print("Finished sampling at element {}".format(i))
            return sample


def generate_array():
    return [random.randint(0, 20) for i in range(2312)]

array = generate_array()
sample = random_sampling(array, 50)
sample = reservoir_sampling(array, 3000)
print(sample)