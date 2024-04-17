#Two Sum Problem [O(n^2)]
        
def two_sum(num_list, target_value):
    # iterate over each number in the list
    for i in range(len(num_list)):
        # iterate over subsequent numbers in the list
        for j in range(i + 1, len(num_list)):
            # check if their sum equals the target value
            if num_list[i] + num_list[j] == target_value:
                # return the indices of the two numbers
                return [i, j]
    
num_list = input("Enter the list of numbers: ").split()
num_list = [int(num) for num in num_list]
target_value = int(input("Enter the target value: "))
      
result = two_sum(num_list, target_value)
        
# print the result
print(result)
