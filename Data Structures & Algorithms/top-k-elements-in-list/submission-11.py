# class Solution:
#     def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#         """
#         build freq hashmap
#         then create a bucket list
#         freq of each item from hashmap becomes its index in the bucket list
#         traverse bucket list in reverse (considering only non empty items)
#         first k items you reach are the answer
#         """

#         hashmap = {}
#         for i in nums:
#             hashmap[i] = hashmap.get(i, 0) + 1

#         # print(hashmap)
#         buckets = [[] for _ in range(len(nums )+1)]

#         for num, freq in hashmap.items():
#             buckets[freq].append(num)

#         # print(buckets)
#         lst = []
#         for j in range(len(buckets) - 1, -1, -1):
#             if len(buckets[j]) > 0:
#                 for l in buckets[j]:
#                     lst.append(l)
#                     if len(lst) == k:
#                         return lst

import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Build the frequency hash map (same as before)
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # Step 2: Build the Min-Heap
        heap = []
        for num, freq in count.items():
            # In Python, heaps sort by the first item in a tuple.
            # So we push (frequency, number) to sort by frequency!
            heapq.heappush(heap, (freq, num))
            print("pushed",heap)
            
            # If our VIP club has more than k elements, kick out the smallest
            if len(heap) > k:
                heapq.heappop(heap)
            print("popped",heap)

                
        # Step 3: Extract the surviving numbers from the heap
        # The heap contains tuples like (frequency, num), we just want the num
        result = []
        for pair in heap:
            result.append(pair[1])
            
        return result