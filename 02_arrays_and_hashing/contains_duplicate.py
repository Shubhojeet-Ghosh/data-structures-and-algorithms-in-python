from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        
        for item in nums:
            if item in seen:
                return True
            
            seen.add(item)
        
        return False

solution = Solution()
print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))