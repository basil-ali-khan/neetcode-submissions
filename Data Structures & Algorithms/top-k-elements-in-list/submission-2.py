class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Build the frequency hash map
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # Step 2: Create buckets (Index = Frequency, Value = List of numbers)
        # Array size is len(nums) + 1 to prevent out-of-bounds errors
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
            
        # Step 3: Read backwards to get the most frequent elements first
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                # The exact second we have our k elements, stop and return!
                if len(result) == k:
                    return result