#Radix Sort

def radix_sort(lst):
    # Find the maximum number to know number of digits
    max1 = max(lst)
    
    length = len(str(max1))
    
    #Apply counting sort to sort elements based on significant place value
    place = 1
    for i in range(length):
        counting_sort(lst, place)
        # Multiply place by 10 to get the next significant place
        place *= 10
    return lst

def counting_sort(lst, place):
    n = len(lst)
    # Create an output list to store the sorted elements
    output = [0] * n
    # Create a counting list to store the count of each digit (0 to 9)
    count = [0] * 10
    
    # Count the frequency of each digit in the appropriate place
    for i in range(0, n):
        index = lst[i] // place
        count[index % 10] += 1
    
    # Change counting_list so that it contains the actual position of each digit 
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build the output list  
    i = n - 1
    while i >= 0:
        index = lst[i] // place
        output[count[index % 10] - 1] = lst[i]
        count[index % 10] -= 1
        i -= 1
    
    # Copy the output list to the original list
    for i in range(0, len(lst)):
        lst[i] = output[i]
        
    
data_list = list(map(int, input().split()))
sorted_list = radix_sort(data_list)
print(sorted_list)

    

