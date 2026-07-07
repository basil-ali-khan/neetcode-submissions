from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for i in nums:
            d[i] += 1

        # print(d)  
        priority_queue = []

        for num, count in d.items():
            heapq.heappush(priority_queue, ((-1 * count), num))

        # print(priority_queue)
        result = []
        for i in range(k):
            popped = heapq.heappop(priority_queue)
            # result.append(popped[1])
            result = result + [popped[1]]
        return result

