4.class Solution:    
    def findUnion(self, a, b):
        a = set(a)
        b = set(b)
        union_set = a.union(b)
        union_list = sorted(list(union_set))
        return union_list
