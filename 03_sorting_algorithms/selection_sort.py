class Solution():
    def selectionSort(self,arr):
        n = len(arr)
        
        for i in range(n-1):
            min_element_index = i
            for j in range(i+1,n):
                if(arr[j] < arr[min_element_index]):
                    min_element_index = j
            
            arr[i],arr[min_element_index] = arr[min_element_index],arr[i]
            print(f"Array after pass : {i+1}  , {arr}")

        return arr

unsorted_array = [5, 3, 8, 4, 2]
print(f"Unsorted Array : {unsorted_array}")

solution = Solution()
sorted_array = solution.selectionSort(unsorted_array)

print(f"Sorted Array : {sorted_array}")