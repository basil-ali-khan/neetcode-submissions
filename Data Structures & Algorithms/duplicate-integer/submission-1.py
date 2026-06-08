class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j:
        #             if nums[i] == nums[j]:
        #                 return True

        # return False
        d = {}
        for i in nums:
            if i in d.keys():
                return True
            d[i] = 1
        return False