class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
                
            # Case 1: Left half is perfectly sorted
            if nums[l] <= nums[mid]:
                # Check if target sits inside the sorted left half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # Search left
                else:
                    l = mid + 1  # Search right
                    
            # Case 2: Right half is perfectly sorted
            else:
                # Check if target sits inside the sorted right half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # Search right
                else:
                    r = mid - 1  # Search left
                    
        return -1