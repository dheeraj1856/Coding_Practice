#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
        if n == 0 or (s == 0 and 0 not in arr):
            return [-1]

        left = 0
        current_sum = arr[0] if n > 0 else 0
        
        # Start from the first element if array is not empty
        right = 1

        while right <= n:
            # Adjust the current sum to be less than or equal to s by moving left pointer
            while current_sum > s and left < right - 1:
                current_sum -= arr[left]
                left += 1
            
            # Check if the current sum matches the target sum
            if current_sum == s:
                return [left + 1, right]  # Return 1-based index

            # Move right pointer and add value to current sum if within array bounds
            if right < n:
                current_sum += arr[right]
            right += 1
        
        # Return [-1] if no subarray is found that matches the sum after full loop
        return [-1]
            
        
