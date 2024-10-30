# KMP Algorithm

def KMP(text, pattern):
    # Length of the text
    lps = computeLPSArray(pattern)
    i = 0
    j = 0
    m = len(pattern)
    n = len(text)
    occurrences = []

    # Iterate through the text
    while i< n:
        # If the pattern matches the text increment both i and j
        if pattern[j] == text[i]:
            i += 1
            j += 1
            # If the pattern is found in the text append the index to the occurrences list
        if j == m:
            occurrences.append(i-j)
            j = lps[j-1]
        elif i<n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return occurrences

def computeLPSArray(pattern):
    
    # Length of the previous longest prefix suffix
    length = 0
    
    # Length of the pattern
    m = len(pattern)
    
    # Initialize the lps array
    lp = [0]
    
    for i in range(1, m):
        if pattern[i] == pattern[length]:
            length += 1
            lp.append(length)
        elif pattern[i] == pattern[length]:
            length = lp[length-1]
            lp.append(length)
        else:
            lp.append(0)
            
    return lp

text = input()
pattern = input()
occurrences = KMP(text, pattern)

for occurence in occurrences:
    end = occurence + len(pattern) -1  
    print(f"Matching Pattern: index {occurence} to {end}.")