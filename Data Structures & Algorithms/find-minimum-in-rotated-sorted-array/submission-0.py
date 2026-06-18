class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            
            # If mid element is greater than the rightmost element, 
            # the minimum must be on the right side.
            if nums[mid] > nums[r]:
                l = mid + 1
            # Otherwise, the minimum is on the left side (including mid)
            else:
                r = mid
                
        return nums[l]