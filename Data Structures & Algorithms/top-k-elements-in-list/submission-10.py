class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        build freq hashmap
        then create a bucket list
        freq of each item from hashmap becomes its index in the bucket list
        traverse bucket list in reverse (considering only non empty items)
        first k items you reach are the answer
        """

        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1

        # print(hashmap)
        buckets = [[] for _ in range(len(nums )+1)]

        for num, freq in hashmap.items():
            buckets[freq].append(num)

        # print(buckets)
        lst = []
        for j in range(len(buckets) - 1, -1, -1):
            if len(buckets[j]) > 0:
                for l in buckets[j]:
                    lst.append(l)
                    if len(lst) == k:
                        return lst