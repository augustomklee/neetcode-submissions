class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for n in nums:
            if n in count:
                return not count[n]
            count[n] = False
        return False