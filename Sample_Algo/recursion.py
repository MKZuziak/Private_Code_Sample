def simple_countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        simple_countdown(i-1)

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

x = fact(3)
print(x)