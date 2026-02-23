51.class Solution:
    def has132Pattern(self, arr):
        stack=[]
        third=float('-inf')
        
        for num in reversed(arr):
            if num < third:
                return True
            while stack and num > stack[-1]:
                third=stack.pop()
            stack.append(num)
        
        return False
