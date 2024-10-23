# Bucket Sort

from Selection_Sort import selection_sort

def bucket_sort(lst):
    # Find the range of the bucket
    min_value = min(lst)
    max_value = max(lst)
    range_value = (max_value - min_value) + 1  # Ensure range is non-zero
    
    # Number of buckets to create
    bucket_count = len(lst) // 2 + 1  # Adjust bucket count as needed
    
    # Create empty buckets
    buckets = [[] for _ in range(bucket_count)]
    
    # Fill the buckets
    for i in lst:
        index = (i - min_value) * (bucket_count - 1) // range_value
        buckets[index].append(i)

    # Sort the buckets
    sorted_lst = []
    for bucket in buckets:
        selection_sort(bucket)
        sorted_lst.extend(bucket)
    
    return sorted_lst

data_list = list(map(int, input().split()))
print(bucket_sort(data_list))



