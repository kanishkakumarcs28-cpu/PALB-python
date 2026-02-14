24.#User function Template for python3
class Solution:
        
    def minSwap (self,arr, k) : 
        n = len(arr)
        good = 0
        for num in arr:
           if num <= k:
              good += 1
        bad = 0
        for i in range(good):
            if arr[i] > k:
               bad += 1

        min_swaps = bad
        for i in range(1, n - good + 1):
             if arr[i - 1] > k:
                 bad -= 1
             if arr[i + good - 1] > k:
                  bad += 1
        min_swaps = min(min_swaps, bad)
        return min_swaps

    


    

