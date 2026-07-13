class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        lst = []
        
        for i in range(len(nums)):
            print("nums[i]", nums[i])
            j = i + 1
            k = len(nums) - 1
            while j < k:
                # print("nums[j]", nums[j], "nums[k]", nums[k])
                
                sum = nums[i] + nums[j] + nums[k]
                if (nums[i] + nums[j] + nums[k]) == 0:
                    l = [nums[i], nums[j], nums[k]]
                    if l not in lst:
                        lst.append(l)
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1

        return lst
