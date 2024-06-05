#Insertion Sort
def insertion_sort(lst):
    n = len(lst)
    # Traverse through 1 to len(lst) as 0th element is already sorted
    for i in range(1,n):
        Key = lst[i]
        # j is the index of the element before Key
        j = i-1
        # Move elements of lst[0..i-1], that are greater than key, to one position ahead of their current position
        while j >=0 and Key < lst[j]:
            # Shift elements to its right
            lst[j + 1] = lst[j]
            # Decrement j by 1 to compare with previous element
            j -= 1
        # Insert Key at its correct position
        lst[j + 1] = Key
    return lst
data_list = list(map(int, input().split()))
print(insertion_sort(data_list))

