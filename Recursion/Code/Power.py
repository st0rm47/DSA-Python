# Power of a number using recursion

def power(base,power):
    # Base case
    if power == 0:
        return 1
    # Recursive case
    return base * power(base,power-1)

print(power(2,3))