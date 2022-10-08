from functools import wraps

import time
import math

def calculate_time(func):

    def inner1(*args, **kwargs):
        # sets the starting time of function
        begin = time.time()
         
        func(*args, **kwargs)
        # sets the end time of the function
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
 
    return inner1

@calculate_time
def factorial(num):
 
    time.sleep(2)
    print(math.factorial(num))

def sarcastic_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return f'Oh Sure, "{orig_val}" sounds like a "great" idea'

    return wrapper

