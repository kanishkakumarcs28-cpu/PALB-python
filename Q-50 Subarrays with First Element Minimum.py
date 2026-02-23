50.class Solution:
    def countSubarrays(self, arr):
        n=len(arr)
        stack=[]
        nextSmaller=[n]*n
        
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if stack:
                nextSmaller[i]=stack[-1]
            stack.append(i)
        
        count=0
        for i in range(n):
            count+=nextSmaller[i]-i
        
        return count
