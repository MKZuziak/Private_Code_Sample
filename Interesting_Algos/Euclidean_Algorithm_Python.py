def greatest_common_divisor(n1: int, n2: int) -> int:        
    # Assertion case
    if n2 > n1:
        n1, n2 = n2, n1     
    
    remainder = n1 % n2
    if remainder == 0:
        return n1
    else:
        return greatest_common_divisor(n2, remainder)

a = greatest_common_divisor(105, 33)
print(a)