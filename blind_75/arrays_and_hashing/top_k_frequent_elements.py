# Time complexity - O(n log n)
def topKFrequent(nums, k):
    freq = {}
    for i,num in enumerate(nums):
        if num in freq:
            freq[num] += 1

        else:
            freq[num] = 1    

    print(freq)

    num_list = []
    for key,val in freq.items():
        num_list.append([val,key])

    print(num_list)

    num_list.sort()
    print(num_list)

    result_list = []
    for i in range(0,k):
        num = num_list.pop()[1]
        print(num)
        result_list.append(num)

    return result_list

nums = [9,4,9,2,9,2,3,3,2,2,2]
k = 2

result = topKFrequent(nums, k)
print(result)