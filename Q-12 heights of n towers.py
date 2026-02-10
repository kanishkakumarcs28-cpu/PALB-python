12.class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()

        ans = arr[-1] - arr[0]

        smallest = arr[0] + k
        largest = arr[-1] - k

        for i in range(1, n):
            if arr[i] - k < 0:
                continue

            mn = min(smallest, arr[i] - k)
            mx = max(largest, arr[i - 1] + k)

            ans = min(ans, mx - mn)

        return ans
