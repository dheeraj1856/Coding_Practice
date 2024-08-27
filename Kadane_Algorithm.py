class Solution:
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        if N == 0:
            return 0
        
        max_current = max_global = arr[0]
        
        for i in range(1, N):
            max_current = max(arr[i], max_current + arr[i])
            if max_current > max_global:
                max_global = max_current
                
        return max_global
