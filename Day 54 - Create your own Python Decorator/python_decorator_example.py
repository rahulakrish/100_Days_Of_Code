import time

def time_decorator(my_function):
    
    def calculate_time():
        start_time = time.time()
        my_function()
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        return float(elapsed_time)

    return calculate_time
        

@time_decorator
def fast_function():
    for i in range(1000):
        i*i

@time_decorator
def slow_function():
    for i in range(10000):
        i*i
    
time_difference = slow_function() - fast_function()
print(time_difference)

#how to interpret @:
#fast_function = time_decorator(fast_function)