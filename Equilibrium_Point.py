# Given an array arr of non-negative numbers. The task is to find the first equilibrium point in an array. 
# The equilibrium point in an array is an index (or position) such that the sum of all elements before that index is the same as the sum of elements after it.
# Note: Return equilibrium point in 1-based indexing. Return -1 if no such point exists. 


class Solution:
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,arr):
        # Your code here
        if len(arr) == 1:
            return 1
        
        total_sum = sum(arr)
        left_sum = 0
        
        for i in range(len(arr)):
            right_sum = total_sum - left_sum - arr[i]
            
            if left_sum == right_sum:
                return i + 1
            
            left_sum += arr[i]
        
        return -1
        

