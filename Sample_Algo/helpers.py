def compare_results(func, func_built, array):
    x_func = func(array)
    x_built = func_built(array)
    print('Comparing results for {} and {}'.\
        format(func, func_built))
    print("Function output {}, Built-in function output: {}, Identical {}".\
        format(x_func, x_built, x_func == x_built))