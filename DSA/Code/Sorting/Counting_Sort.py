#Counting Sort

def counting_sort(lst):
    # Find the maximum element in the list
    max_element = max(lst)
    # Create a counting list to store the count of each element
    counting_list = [0] * (max_element + 1)
    # Count the frequency of each element
    for i in lst:
        counting_list[i] += 1
    # Create a sorted list to store the sorted elements
    sorted_list = []
    # Append the element the number of times it appears in the counting list
    for i in range(len(counting_list)):
        sorted_list.extend([i] * counting_list[i])
    return sorted_list
data_list = list(map(int, input().split()))
sorted_list = counting_sort(data_list)
print(sorted_list)

#Count Unique Elements in the List
