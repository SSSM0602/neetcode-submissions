class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, curList, total):
            if total == target:
                res.append(curList.copy())
                return 
            elif i >= len(nums) or total > target:
                return
            
            curList.append(nums[i])
            dfs(i, curList, total + nums[i])

            curList.pop()
            dfs(i + 1, curList, total)
        dfs(0, [], 0)
        return res

                