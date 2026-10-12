class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i, num in enumerate(nums):
            prod = 1
            for j in range(len(nums)):
                if j != i:
                    prod *= nums[j]
            res[i] = prod
        return res

        