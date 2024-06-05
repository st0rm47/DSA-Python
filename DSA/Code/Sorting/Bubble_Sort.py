#Bubble Sort(Ascending Order)
def bubble_sort(lst):
    n = len(lst)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted
        for j in range(n-1):
            # Swap if the element found is greater
            if lst[j] > lst[j+1]:
                # Swap the elements
                lst[j], lst[j+1] = lst[j+1], lst[j]   
    return lst
data_list = list(map(int, input().split()))
print(bubble_sort(data_list))


#Bubble Sort(Descending Order)
def bubble_sort(lst):
    n = len(lst)
    # Traverse through all array elements 
    for i in range(n-1):
        # To check if any swap is done in the inner loop
        swapped = False
        # Last i elements are already sorted
        for j in range(n-1-i):
            # Swap if the element found is greater
            if lst[j] < lst[j+1]:
                # Swap the elements
                lst[j], lst[j+1] = lst[j+1], lst[j]  
                swapped = True
        if not swapped:
            break
    return lst
data_list = list(map(int, input().split()))
print(bubble_sort(data_list))
