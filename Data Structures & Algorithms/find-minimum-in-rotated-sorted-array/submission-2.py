class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[r] < nums[l]:
                r -= 1
            else:
                try:
                    return nums[r + 1]
                except:
                    return nums[l]



        