class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       res = dict() 
       for i in range(len(nums)):  
            if nums[i] in res: 
                return True
            res[nums[i]] = 0
            
       return False