#Merge Sort
def merge_sort(lst):
    n = len(lst)
    # Find the middle index
    mid = n//2
    # Base case
    if n<=1:
        return lst
    # Divide the list into two halves
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    # Merge the two halves
    return merge(left, right)

def merge(left, right):
    # Create an empty list to store the result
    result = []
    # Create two pointers for left and right list
    i = 0
    j = 0
    # Traverse through the left and right list
    while i<len(left) and j<len(right):
        # Compare the elements of left and right list
        if left[i] < right[j]:
            # Append the smaller element to the result list
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append the remaining elements of left list
    result.extend(left[i:])
    # Append the remaining elements of right list
    result.extend(right[j:])
    return result

data_list = list(map(int, input().split()))
print(merge_sort(data_list))



# Nth Smallest Element of Two Sorted List
def find_smallest_number(nums1, nums2, n):
    result = []
    # Create two pointers for left and right list
    i = 0
    j = 0
    # Traverse through the left and right list
    while i<len(left) and j<len(right):
        # Compare the elements of left and right list
        if left[i] < right[j]:
            # Append the smaller element to the result list
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append the remaining elements of left list
    result.extend(left[i:])
    # Append the remaining elements of right list
    result.extend(right[j:])
    if n <= len(result):
        return result[n-1]
    
# take integer inputs and convert it to a list
left = list(map(int, input().split()))
# take integer inputs and convert it to a list
right = list(map(int, input().split()))
# take integer input
n = int(input())
result = find_smallest_number(left, right, n)
print(result)

