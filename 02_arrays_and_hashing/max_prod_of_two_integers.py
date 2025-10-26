
def max_product(arr):
    max_prod = 1
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            prod = arr[i] * arr[j]
            if(prod > max_prod):
                max_prod = prod
        
    return max_prod        
        

print(max_product([1, 7, 3, 4, 9, 5]))