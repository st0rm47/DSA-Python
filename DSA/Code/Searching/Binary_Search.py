#Binary Search

def binary_search(lst, key):
    n = len(lst)
    # low and high keep track of which part of the list you'll search in.
    low = 0
    high = n - 1
    # While you haven't narrowed it down to a single element ...
    while low <= high:
        # ... check the middle element
        mid = (low + high) // 2
        # Found the key
        if lst[mid] == key:
            return mid
        # The key is in the lower half
        elif lst[mid] < key:
            return binary_search(lst[mid+1:], key)
        # The key is in the upper half
        else:
            return binary_search(lst[:mid], key)
    return None

data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
key = 7
print(binary_search(data, key))