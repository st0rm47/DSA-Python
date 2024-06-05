#Quick Sort
def quick_sort(lst):
    n = len(lst)
    #base case
    if n <= 1:
        return lst
    else:
        #pop the first element as pivot
        pivot = lst.pop(0)
    right = []
    left = []
    for x in lst:
        if x > pivot:
            #append the element to the right list
            right.append(x)
        else:
            #append the element to the left list
            left.append(x)
    #recursively call the quick_sort function on the left and right list
    return quick_sort(left) + [pivot] + quick_sort(right)

data_list = list(map(int, input().split()))
sorted_list = quick_sort(data_list)
print(sorted_list)