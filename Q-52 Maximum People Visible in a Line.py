52.class Solution:
    def maxPeople(self, arr):
        n = len(arr)
        
        def count_visible(a):
            res = [0] * n
            stack = []
            for i in range(n):
                res[i] = 1 
                while stack and a[i] > stack[-1][0]:
                    res[i] += res[stack.pop()[1]]
                stack.append((a[i], i))
            return res
        left = arr[::-1]
        left_visible = count_visible(left)[::-1]
        right_visible = count_visible(arr)
        total = [left_visible[i] + right_visible[i] - 1 for i in range(n)]
        return max(total)
