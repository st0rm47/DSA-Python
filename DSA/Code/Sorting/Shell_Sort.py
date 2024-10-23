#Shell Sort

def shell_sort(arr):
    
    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = n//2
    
    # Do a gapped insertion sort for this gap size.
    # The first gap elements arr[0..gap-1] are already in gapped order
    # keep adding one more element until the entire array is gap sorted
    
    while gap > 0:
        for i in range(gap,n):

            key = arr[i]
            # Keep track of the index of the element before key
            j = i
            # Move elements of arr[0..i-gap], that are greater than key, to one position ahead of their current position
            while j >= gap and arr[j-gap] > key:
                arr[j] = arr[j-gap]
                j -= gap
            # Insert key at its correct position
            arr[j] = key    
        gap //= 2
    

arr = [12, 34, 54, 2, 3]
shell_sort(arr)
print("Sorted array is:", arr)
