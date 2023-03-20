import timeit

a=2
b=3
tolerance =1e-6
max_iterations =100
count=0

def sol(x):
    return x**4 - x**3 -10


def bisection():
    # access the variables outside the function
    global a,b, count

    for i in range(max_iterations): 
        c=(a+b)/2
        count +=1
        if abs(sol(c)) < tolerance:
            print(f"Root found at x = {c:.6f}")
            break
        elif sol(c)*sol(a)<0 :
            b=c
        else:
            a=c


# measure the execution time of bisection
execution_time = timeit.timeit(bisection, number=1)

# Print the execution time
print(f"Execution time: {execution_time:.5f} seconds")

#print count/no of iterations
print(f"count is: {count} in total")


