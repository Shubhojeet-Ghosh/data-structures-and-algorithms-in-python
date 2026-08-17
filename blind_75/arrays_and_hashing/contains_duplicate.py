# brute force
# def hasDuplicate(nums) -> bool:
#     for i in range(0,len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if nums[i] == nums[j]:
#                 return True

#     return False
        


# optimized solution
# def hasDuplicate(nums) -> bool:
#         seen = []
#         for num in nums:
#             if num in seen:
#                 return True

#             seen.append(num)

#         return False

# most optimized solution
def hasDuplicate(nums) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False

nums = [1, 2, 3, 3]
# nums = [1, 2, 3, 4]

result = hasDuplicate(nums)
print(result)