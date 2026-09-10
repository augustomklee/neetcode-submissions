class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m = len(nums) // 2
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[m] == target:
                return m
            # Target is bigger
            if nums[m] < target: 
                l = m + 1
            # Target is smaller
            else:
                r = m - 1
            m = ((r - l) // 2) + l
        return -1