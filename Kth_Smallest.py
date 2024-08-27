# Given an array arr[] and an integer k where k is smaller than the size of the array, the task is to find the kth smallest element in the given array. It is given that all array elements are distinct.
# Follow up: Don't solve it using the inbuilt sort function.


class Solution:

    def kthSmallest(self, arr,k):
        def quickselect(left, right, k):
            if left == right:
                return arr[left]
            
            pivot_index = left
            pivot_index = partition(left, right, pivot_index)
            
            if k == pivot_index:
                return arr[k]
            elif k < pivot_index:
                return quickselect(left, pivot_index - 1, k)
            else:
                return quickselect(pivot_index + 1, right, k)
        
        def partition(left, right, pivot_index):
            pivot_value = arr[pivot_index]
            arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
            store_index = left
            
            for i in range(left, right):
                if arr[i] < pivot_value:
                    arr[store_index], arr[i] = arr[i], arr[store_index]
                    store_index += 1
            
            arr[right], arr[store_index] = arr[store_index], arr[right]
            return store_index
        
        return quickselect(0, len(arr) - 1, k - 1)
        

