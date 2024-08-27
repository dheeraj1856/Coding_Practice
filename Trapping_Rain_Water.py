# Given an array arr[] of N non-negative integers representing the height of blocks.
# If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 
# Input:
# N = 4
# arr[] = {7,4,0,9}
# Output:
# 10
# Explanation:
# Water trapped by above 
# block of height 4 is 3 units and above 
# block of height 0 is 7 units. So, the 
# total unit of water trapped is 10 units.

class Solution:
    def trappingWater(self, arr,n):
        #Code here
        if n <= 2:
            return 0  
        
        left_max = [0] * n
        right_max = [0] * n
        
        # Fill left_max array
        left_max[0] = arr[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], arr[i])
        
        # Fill right_max array
        right_max[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], arr[i])
        
        # Calculate the trapped water
        trapped_water = 0
        for i in range(n):
            trapped_water += min(left_max[i], right_max[i]) - arr[i]
        
        return trapped_water        
