# Palindrome using recursion

def is_palindrome(s):
    if len(s) == 1 or s == "":
        return True
    
    # Compare the first and last characters
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False
    
s = input("Enter a string: ")
result = is_palindrome(s)
print(result)