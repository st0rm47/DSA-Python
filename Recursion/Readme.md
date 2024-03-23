# Recursion

## What is Recursion?
Recursion is a method where the solution to a problem depends on solutions to smaller instances of the same problem.

## How does Recursion work?
Recursion works by breaking down a problem into smaller, more manageable problems. It then solves each of these smaller problems and combines the results.

![alt text](image.png)

## Exampls of Recursion
```python
def print_numbers(n):
    if n == 4:
        return "Done"   
    print(n)
    return print_numbers(n + 1)
 
output = print_numbers(1)
print(output)
```

![alt text](image-1.png)