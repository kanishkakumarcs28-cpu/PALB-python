15.class Solution:
    def mergeArrays(self, a, b):
        n = len(a)
        m = len(b)
        
        i = n - 1
        j = 0
        
        # Step 1: Swap elements if needed
        while i >= 0 and j < m:
            if a[i] > b[j]:
                a[i], b[j] = b[j], a[i]
                i -= 1
                j += 1
            else:
                break
        
        # Step 2: Sort both arrays
        a.sort()
        b.sort()
