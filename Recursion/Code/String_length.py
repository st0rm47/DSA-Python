# Length of string using recursion

def string_length(s):
    if s == "":
        return 0
    
    # Count the first character and recur on the rest of the string
    return 1 + string_length(s[1:])

s = input("Enter a string: ")
result = string_length(s)
print(result)