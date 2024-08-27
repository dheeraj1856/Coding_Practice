# Given an array arr. Find the majority element in the array. If no majority exists, return -1.
# A majority element in an array of size n is an element that appears strictly more than n/2 times in the array.

#User function template for Python 3
from collections import Counter 
class Solution:
    def majorityElement(self, A, N):
        #Your code here
        if N == 1:
            return A[0]  
        count = Counter(A)
        max_count = max(count.values())
        
        for key, value in count.items():
            if value == max_count:
                majority_element = key
                break

        if max_count > N // 2:
            return majority_element
        else:
            return -1
            
            
        
            
