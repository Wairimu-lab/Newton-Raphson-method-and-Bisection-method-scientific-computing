
import timeit

x0=1
tolerance=1e-6
max_iteration = 100
count =0

# Define the function
def func(x):
    return x**4 - x**3 -10


# Define the function's derivative
def der(x):
    return 4*x**3 - 3*x**2


# Define the Newton-Raphson method
def newton_raphson():
    global x0, count,tolerance,max_iteration
    for i in range (max_iteration):
        x1 =x0 -func(x0)/der(x0)
        count+=1
        if abs (func(x1)) < tolerance:
            print(f"Root found at x = {x1:.6f}")
            break
        else:
            x0 = x1


# Measure the execution time of newton_raphson
execution_time = timeit.timeit(newton_raphson, number=1)

# Print the execution time
print(f"Execution time: {execution_time:.5f} seconds")

print(f"count is: {count} in total")


