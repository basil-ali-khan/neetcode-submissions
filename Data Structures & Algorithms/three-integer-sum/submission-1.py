class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort() sorts the list in-place; do not assign it to a variable
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            # Skip duplicate values for the first element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Initialize pointers at opposite ends of the remaining array
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if total < 0:
                    # Sum is too small; move the left pointer rightward to get a bigger value
                    j += 1
                elif total > 0:
                    # Sum is too large; move the right pointer leftward to get a smaller value
                    k -= 1
                else:
                    # Found a valid triplet
                    result.append([nums[i], nums[j], nums[k]])
                    
                    # Move pointers and skip duplicate values for j and k
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                        
        return result