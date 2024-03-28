from functools import reduce

# Generating Fibonacci series using lambda function
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])

# Generate Fibonacci series with 50 elements
fib_series = fib(50)

# Print the Fibonacci series
print(fib_series)
