class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                x = num
                streak = 1
                while x + 1 in nums:
                    x += 1
                    streak += 1
                    
                
                longest = max(longest, streak)
        return longest
