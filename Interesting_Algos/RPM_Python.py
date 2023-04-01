import math
import pandas as pd

def rpm(n1: int, n2: int) -> int:
    halving = [n1]
    while halving[-1] > 1:
        halving.append(math.floor(halving[-1] / 2))
    
    doubling = [n2]
    while len(doubling) < len(halving):
        doubling.append(doubling[-1] * 2)
    
    half_double = pd.DataFrame(zip(halving, doubling))
    half_double = half_double.loc[half_double[0]%2 == 1,:]
    answer = sum(half_double.loc[:,1])

    return answer

answer = rpm(n1=89, n2=18)
print(answer)