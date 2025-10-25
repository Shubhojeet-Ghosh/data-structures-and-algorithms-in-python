
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for idx,num in enumerate(nums):
            complementary = target - num
            if complementary in seen:
                return [idx,seen[complementary]]

            seen[num] = idx

solution = Solution()
print(solution.twoSum([2,7,11,15],9))