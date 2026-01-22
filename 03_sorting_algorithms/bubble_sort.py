class Solution:
    def bubbleSort(self,arr):
        for i in range(0,len(arr)):
            swapped = False
            for j in range(0,len(arr)-i-1):
                  if(arr[j] > arr[j+1]):
                       arr[j],arr[j+1] = arr[j+1],arr[j]
                       swapped = True


            if(swapped is False):
                print(f"Array already sorted in step : {i}")
                break
                 
        return arr


array_to_sort = [64, 34, 25, 12, 22, 11, 90]
solution = Solution()
sorted_array = solution.bubbleSort(array_to_sort)
print(f"Sorted Array : {sorted_array}")