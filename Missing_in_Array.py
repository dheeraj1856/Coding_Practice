# Given an array arr of size n−1 that contains distinct integers in the range of 1 to n (inclusive), find the missing element. 
# The array is a permutation of size n with one element missing. Return the missing element.

class Solution:
    def missingNumber(self,array,n):
        # code here
        #A[] = sorted(arr)
        #check = A[0]
        #while i < n:
        #    if A[i+1] == (check + 1):
        #        i+=1
        #    else:
        #        return [ i+1 ]
                
        
        total_sum = n * (n + 1)//2
        array_sum = sum(array)
        return total_sum - array_sum
    
