class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
    
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if the needed number has already been seen
            if complement in seen:
                return [seen[complement], i]
            
            # Otherwise, add current number to the dictionary
            seen[num] = i
            
        return [] # Return empty if no solution found