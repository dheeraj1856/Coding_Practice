# Given an array arr of size n which contains elements in range from 0 to n-1, you need to find all the elements occurring more than once in the given array. 
# Return the answer in ascending order. If no such element is found, return list containing [-1]. 

class Solution:
    def duplicates(self, arr, n): 
        # code here
        for i in range(n):
            index = arr[i] % n
            arr[index] += n
        
        final_array = []
        for i in range(n):
            if arr[i] // n > 1:
                final_array.append(i)
        
        if not final_array:
            return [-1]
        
        return final_array
            
