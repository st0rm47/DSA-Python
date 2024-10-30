#Two Sum Problem [O(n)]

def two_sum(num_list, target_value):
    dictionary = {}
    for index, value in enumerate(num_list): 
        # add items of num_list to dictionary
        # value as key and index as value
        dictionary[value] = index

    for i in range(len(num_list)):
        complement = target_value - num_list[i]
        
        # check if item's complement is present in dictionary
        if complement in dictionary and dictionary[complement] != i:
            
            # return element index and complement's index
            return [i, dictionary[complement]]
    
num_list = [2, 7, 11, 15]
target_value = 9
    
result = two_sum(num_list, target_value)
print(result) 
 