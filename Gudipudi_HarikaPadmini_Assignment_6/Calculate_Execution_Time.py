"""
HW      # 6
Problem # 1 Calculate_Execution_Time
Author  # Gudipudi HarikaPadmini
"""
import time


# Using decorator by this decorator we can wrap another function in a function
def decorator(func):
    def wrapper(*args, **kwargs):  # parameters are passed as args ,kwargs like tuple and dictionary respectively.
        start_time = time.time()  # unix time is from time module
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function execution time: {elapsed_time:.2f} seconds elapsed")
        return result

    return wrapper


@decorator
def test(n):    # function to pass a parameter to the decorator function
    for i in range(n):
        pass


test(1000000)
