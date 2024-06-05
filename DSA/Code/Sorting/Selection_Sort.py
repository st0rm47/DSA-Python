#Selection Sort
def selection_sort(lst):
    n = len(lst)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        # Traverse through the unsorted array
        for j in range(i+1, n):
            # Compare the current element with the minimum element
            if lst[j] < lst[min_index]:
                # Update the index of minimum element
                min_index = j
        # Swap the found minimum element with the first element
        lst[i], lst[min_index] = lst[min_index], lst[i]  
    return lst
data_list = list(map(int, input().split()))
print(selection_sort(data_list))

#Selection Sort(Swap Count)
def selection_sort(lst):
    n = len(lst)
    swap = 0
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        # Traverse through the unsorted array
        for j in range(i+1, n):
            # Compare the current element with the minimum element
            if lst[j] < lst[min_index]:
                # Update the index of minimum element
                min_index = j
        if min_index !=i:
            # Swap the found minimum element with the first element
            lst[i], lst[min_index] = lst[min_index], lst[i]
            swap +=1
    return swap
data_list = list(map(int, input().split()))
print(selection_sort(data_list))
