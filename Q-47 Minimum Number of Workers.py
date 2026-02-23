47.class Solution:
    def minMen(self, arr):
        n = len(arr)
        intervals = []
        
        for i in range(n):
            if arr[i] != -1:
                l = max(0, i - arr[i])
                r = min(n - 1, i + arr[i])
                intervals.append((l, r))
        
        intervals.sort()
        
        count = 0
        curr = 0
        i = 0
        
        while curr < n:
            farthest = curr - 1
            
            while i < len(intervals) and intervals[i][0] <= curr:
                farthest = max(farthest, intervals[i][1])
                i += 1
            
            if farthest < curr:
                return -1
            
            count += 1
            curr = farthest + 1
        
        return count
