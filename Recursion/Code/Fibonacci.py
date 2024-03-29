# Fibonacci series using recursion

def fibonacci(n):
    # Base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recursive case
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))