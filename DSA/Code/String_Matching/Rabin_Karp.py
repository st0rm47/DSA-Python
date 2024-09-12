def compute_hash(text, length):
    hash_val = 0
    for i in range(length):
        hash_val += ord(text[i]) * (256 ** (length - i - 1))
    return hash_val

def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    text_hash = compute_hash(text, m)
    pattern_hash = compute_hash(pattern, m)
    for i in range(n - m + 1):
        if text_hash == pattern_hash:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            text_hash = (text_hash - ord(text[i]) * (256 ** (m - 1))) * 256 + ord(text[i + m])
    return -1

text = "AABAACAADAABAABA"