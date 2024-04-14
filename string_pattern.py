def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k - 1]
        if pattern[k] == pattern[q]:
            k += 1
        pi[q] = k
    return pi

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    pi = compute_prefix_function(pattern)
    q = 0
    matches = []
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
            print(q)
        if pattern[q] == text[i]:
            q += 1
            print(q)
        if q == m:
            print(q)
            matches.append(i - m + 1)
            q = pi[q - 1]
    return matches

# i = 6
# q = 6
# Example usage:
text = "ABABABACABAABABABACABAC"
pattern = "ABABAC"
print("Pattern found at positions:", kmp_search(text, pattern))
