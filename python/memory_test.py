
from memory_profiler import profile

@profile
def my_function():
    a = [i for i in range(10000)]
    b = [i * 2 for i in a]
    del b
    return a

@profile
def another_function():
    x = [i for i in range(10000)]
    y = [i * 3 for i in x]
    del y
    return x

if __name__ == "__main__":
    my_function()
    another_function()
