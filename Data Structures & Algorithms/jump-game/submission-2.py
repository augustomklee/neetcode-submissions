class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        goal = len(nums) - 1
        cur = len(nums) - 2
        while cur >= 0:
            if nums[cur] >= goal - cur:
                goal = cur
            cur -= 1
        return True if goal == 0 else False
        
            