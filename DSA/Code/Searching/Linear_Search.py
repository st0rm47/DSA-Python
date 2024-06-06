#Linear Search

def linear_search(lst,key):
    n = len(lst)
    #Iterate through the list
    for i in range(n):
        #If the key is found, return the index
        if lst[i] == key:
            return i
    return None
data = [1,2,3,4,5,6,7,8,9,10]
key = 5
print(linear_search(data,key))

