class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if(len(s) != len(t)):
            return False
        
        hash_s = {}
        for c in s:
            if c in hash_s:
                hash_s[c] = hash_s[c] + 1

            else:
                hash_s[c] = 1

        for num in t:
            if(num not in hash_s):
                return False
            
            hash_s[num] -= 1
            if(hash_s[num] < 0):
                return False

        return True
    
s = Solution()
print(s.isAnagram("madam","madam"))