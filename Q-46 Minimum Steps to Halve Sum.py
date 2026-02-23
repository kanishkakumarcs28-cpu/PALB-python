46.import heapq
class Solution:
    def minOperations(self, arr):
        total_sum=sum(arr)
        target=total_sum/2
        operations=0
        max_heap=[-x for x in arr]
        heapq.heapify(max_heap)
        current_sum=total_sum
        while current_sum>target:
            largest=-heapq.heappop(max_heap)
            half=largest/2
            current_sum-=half
            heapq.heappush(max_heap,-half)
            operations+=1
        return operations
