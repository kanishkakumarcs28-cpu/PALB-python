29.class Solution:
    def median(self, mat):
        n = len(mat)
        m = len(mat[0])

        def countSmallerOrEqual(row, x):
            l, r = 0, len(row) - 1
            while l <= r:
                mid = (l + r) // 2
                if row[mid] <= x:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        low, high = 1, 10**9
        desired = (n * m) // 2 + 1

        while low < high:
            mid = (low + high) // 2
            cnt = sum(countSmallerOrEqual(row, mid) for row in mat)

            if cnt < desired:
                low = mid + 1
            else:
                high = mid

        return low
