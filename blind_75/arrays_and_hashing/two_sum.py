#  brute force
# def twoSum(nums, target):
#     for i in range(0, len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i,j]


#  optimized
def twoSum(nums, target):
    seen = {}
    for i,num in enumerate(nums):
        compliment = target - num
        if compliment in seen:
            return [seen[compliment], i]

        else:
            seen[num] = i

            
nums = [3,4,5,6] 
target = 7

# nums = [4,5,6]
# target = 10

# nums = [5,5]
# target = 10

result = twoSum(nums, target)
print(result)