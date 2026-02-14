27.class Solution:
    def spirallyTraverse(self, mat):
        result = []
        n = len(mat)
        m = len(mat[0])
        top, left = 0, 0
        bottom, right = n - 1, m - 1

        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                result.append(mat[top][j])
            top += 1

            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1

            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(mat[bottom][j])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1

        return result
