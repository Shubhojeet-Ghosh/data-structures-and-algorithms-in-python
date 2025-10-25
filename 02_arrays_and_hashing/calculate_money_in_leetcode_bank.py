class Solution:
    def totalMoney(self, n: int) -> int:
        cur_week = 1
        sum = 0
        j = 1

        for i in range(1,n+1):

            sum = sum + j
            j = j + 1

            if i % 7 == 0:
                cur_week = cur_week + 1
                j = cur_week

        
        return sum
    
solution = Solution()

print(solution.totalMoney(20))