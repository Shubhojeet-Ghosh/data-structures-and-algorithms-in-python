# sorting approach
# def isAnagram(s: str, t: str) -> bool:
#     if(sorted(s) ==  sorted(t)):
#         return True

#     return False

#  optimized solution
def isAnagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False
    
    freq = {}

    for n in s:
        if n in freq:
            freq[n] = freq[n] + 1

        else:
            freq[n] = 1

    for n in t:
        if n not in freq:
            return False
        
        freq[n] = freq[n] - 1
        if(freq[n] < 0):
            return False

    return True
        


s = "ba"
t = "ab"

result = isAnagram(s, t)
print(result)