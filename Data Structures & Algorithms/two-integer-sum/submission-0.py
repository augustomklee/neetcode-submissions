class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i, n in enumerate(nums):
            if n in count:
                return [count[n], i]
            count[target - n] = i
        return