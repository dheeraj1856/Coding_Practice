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
    
