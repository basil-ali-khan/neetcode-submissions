class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        forward multiply
        1,2,4,6
        1,1,2,8

        backward multiply
        1,6,24,48
        48,24,6,1
        """
        
        forw_prod = [1]
        for i in range(1, len(nums)):
            forw_prod.append(nums[i - 1] * forw_prod[i - 1])
        print(forw_prod)

        back_prod = [1]
        for i in range(len(nums) - 2, -1, -1):
            back_prod.append(nums[i + 1] * back_prod[-1])
        print(back_prod)  

        back_prod.reverse() 

        prod = []

        for i in range(len(nums)):
            prod.append(forw_prod[i] * back_prod[i])

        return prod
