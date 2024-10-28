# This function computes the hash value of a string using the Rabin-Karp algorithm

def compute_hash(string, base = 256, mod = 101):
    #Initialize hash value to 0
    hash_val = 0
    for index, char in enumerate(string):
        
        #Calculate ascii value
        ascii_val = ord(char)   # ord() function returns the ASCII value of the character
        #Calculate the exponent value
        exponent = len(string) - index - 1
        #Calculate the hash value
        hash_val += ascii_val * (base ** exponent)
    return hash_val % mod  

string = "NEPAL"
print(compute_hash(string)) # Output: 14

def rabin_karp(text,pattern,base = 256, mod = 101):
    #Caclulate pattern length and text length
    pattern_len = len(pattern)
    text_len = len(text)
    
    #Calculate the hash value of the pattern
    pattern_hash = compute_hash(pattern)
    
    #Calculate the hash value of the first window of the text
    text_hash = compute_hash(text[:pattern_len])
    
    #Initialize the result list
    result = []
    
    #Iterate through the text
    for index in range(text_len - pattern_len + 1):
        #Check if the hash values match
        if pattern_hash == text_hash:
            #Check if the pattern matches the text
            if pattern == text[index:index+pattern_len]:
                result.append(index)
        #Calculate the hash value of the next window
        if index < text_len - pattern_len:
            #Calculate the base power
            base_power = pow(base, pattern_len - 1) % mod
            #Calculate the hash value of the next window
            text_hash = (base * (text_hash - ord(text[index]) * base_power))
            #Add the next character to the hash value
            text_hash = (text_hash + ord(text[index + pattern_len])) % mod
    return result


text = "NEPALESELIVEINNEPAL"
pattern = "NEPAL"
occcurences = rabin_karp(text,pattern)

for occurence in occcurences:
    end = occurence + len(pattern) -1
    print(f"Macth found at index {occurence} to {end}.") 
    