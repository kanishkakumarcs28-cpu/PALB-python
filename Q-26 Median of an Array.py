26.class Solution:
    def findMedian(self, arr):
         arr.sort()
         n = len(arr)
         if n//2 == 0:
             mid1 = len(n)//2 - 1
             mid2 = len(n)//2
             return(arr[mid1] + arr[mid2]) / 2
             
         else:
             return arr[n//2]
        
            
        
            
