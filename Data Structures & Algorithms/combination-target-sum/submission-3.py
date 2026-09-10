class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, target):
            if target < 0:
                return
            if target == 0:
                res.append(subset.copy())
                return
            if i >= len(nums):
                return

            # include nums[i]
            subset.append(nums[i])
            dfs(i, target - nums[i])

            # don't include nums[i]
            subset.pop()
            dfs(i + 1, target)
        dfs(0, target)
        return res