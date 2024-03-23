# Sum of Natural Numbers using Recursion

def sum_of_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_numbers(n-1)
    
n = int(input("Enter a number: "))
print("Sum of",n ,"numbers:",sum_of_numbers(n))

