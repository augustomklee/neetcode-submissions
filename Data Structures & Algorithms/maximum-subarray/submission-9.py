class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        res = nums[0]
        newSum = 0
        for i in range(len(nums)):
            newSum += nums[i]
            res = max(res, newSum)
            if newSum < 0:
                res = max(res, self.maxSubArray(nums[i + 1:]))
                return res
        return res

        