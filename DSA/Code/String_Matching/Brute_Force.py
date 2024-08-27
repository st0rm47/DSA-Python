def brute_force(text, pattern):
    n = len(text)
    m = len(pattern)
    occurrences = []
    # Loop through the text to find the pattern i.e text[0:m], text[1:m+1], text[2:m+2], ..., text[n-m:n]
    for i in range(n - m + 1):
        # Loop through the pattern to check if it matches the text from i to i + m
        for j in range(m):
            # If the characters don't match, break the loop
            if text[i + j] != pattern[j]:
                break
        # If the loop didn't break, it means the pattern was found
        # Add the index to the list of occurences
        if j == m - 1:
            occurrences.append(i)
            
    return occurrences

# Test the function
text = "CODEWITHCODER"
pattern = "CODE"
print(brute_force(text, pattern))


